
#los parametros de la función son Datos es el nombre de la base de datos
#f11 La variable a filtrar 
#f2 el valor a filtrar 
#c1 las columnas a ver
f1=function(Datos,f11,f2,c1){
  library(tidyverse)
  x=Datos
  y=paste("C:/Users/Antonino/Desktop/",x,sep = "")
  Datos=read.csv2(y)
  Datos=data.frame(Datos)

  data=Datos %>% 
    filter(get(f11)==f2) %>%select(c1)
  
#  data=data.frame(data)
 b1= ggplot(data, aes(x=0 ,y=get(c1[1]))) +  geom_boxplot(fill = "orange", colour = "blue")
 b2=summary(data)
  return(list(b2,b1))
  
}
#ejemplo  se va a tomar la Base1.csv #revisar que este en la carpeta de trabajo del proyecto
#Se filtra la variable SO2 que toma valor 10
# las columnas a ver son Dias, precipitacion y So2
f1("Base1.csv","SO2",10,c("Dias","Precipitación","SO2"))






         