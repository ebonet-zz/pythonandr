
library(ggplot2)
library(RMisc)
library(grid)
library(png)


plot_results <- function(expected, predicted) {
  
  par(mfrow=c(2,1)) 
  
  plot(test_data$rentPrice ~ predicted, 
       xlab = "Valor real (R$)", 
       ylab = "Preço estimado (R$)", 
       col = 'red',
       main = "Relação entre resultados obtidos")
  
  hist(abs(test_data$rentPrice - predicted), 
       breaks = 30, 
       c='red', 
       xlab = "Erro Absoluto (R$)", 
       ylab = "Número de casos", 
       main="Erro de medição")  
}

plot_results_ggplot2 <- function(expected, predicted) {
  
  p1 <- ggplot(data.frame(expected,predicted), aes(x=expected, y=predicted)) +
    xlab("Preço do aluguel") +
    ylab("Preço Estimado") +
    geom_point(colour='red') +
    ggtitle("Relação entre resultados obtidos")
  
  p2 <- ggplot(abs(expected- predicted), aes(x=expected) ) + 
    geom_histogram(fill='red', colour='grey') +
    xlab("Erro absoluto") +
    ylab(" ")
  multiplot(p1, p2, cols=1)
}

plot_map <- function(values) {
  img <- readPNG("flnp2.png")
  img[,,4] <- 0.3
  ggplot(train_data, aes(x=longitude, y=latitude, color = rentPrice) ) +
    scale_colour_gradientn( 
      colours=rev(rainbow(4)), guide = "colourbar") +
    annotation_custom(
      rasterGrob(img, width=unit(1,"npc"), height=unit(1,"npc")), 
      -Inf, Inf, -Inf, Inf) +
    scale_x_continuous(limits = c(-48.68, -48.3))+
    scale_y_continuous(limits = c(-27.85, -27.35))+
    scale_radius(range=c(1,6)) +
    geom_point(aes(size = 1000/ sqrt(train_data$rentPrice)))+
    ggtitle("Distribuição dos Imóveis")
} 