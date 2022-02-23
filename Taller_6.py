from graphics import *

#Recibe como parametro un directorio
def SimularSemiParabolico(Obj):
  '''
    ***Ecuaciones del movimiento Semi-parabolico:***

      Movimiento Horizontal
        1. Distancia(x) = Vel.Inicial(Vo) * Tiempo(t)
        2. Distancia(x) = Vel.Inicial(Vo) * Raiz[2Altura(h) / Gravedad(g)]
      
      Movimiento Vertical
        3. Altura(h) = Alt.Inicial(Yo) - Gravedad(g)/2 * [Distancia(x)**2 / Vel.Inicial(Vo)**2]
        4. Altura(h) = 1/2 * Gravedad(g) * Tiempo(t)**2
      
      Tiempo
      5. Tiempo(t) = Distancia(x) / Vel.Inicial(Vo)
      6. Tiempo(t) = Raiz[2Altura(h) / Gravedad(g)]
  '''
  
  '''Declaración del objeto'''
  #Crea un diccionario vacio
  info = dict()

  
  '''Estructuración de los datos'''
  #Crea el titulo de la gráfica
  info.setdefault('Title', 'Lanzamiento de ' + Obj['name'])
  
  #Almacena la velocidad inicial del lanzamiento
  info.setdefault('Vo', Obj['Vo'])
  
  #Almacena la altura del lanzmiento
  info.setdefault('Altura', Obj['h'])
  
  #Contador para el calculo del tiempo en x cordenada y para dimensionamiento de la ventana gráfica
  info.setdefault('Distancia', 0)

  #Acumulador del tiempo del movimiento
  info.setdefault('Tiempo', 0)

  #Constante de la Gravedad
  info.setdefault('Gravedad', 9.8)

  #Lista vacia que almacna las coordenadas de la gráfica
  info.setdefault('Graphic', list())

  #Agrega tuplas con coordenadas mientras el resultado de la ecuación 3 sea mayor a 0
  while info['Altura'] - (1/2 * info['Gravedad']* (info['Tiempo']** 2)) >= 0:
    
    info['Graphic'].append(
      (
        #Ecuación 1
        info['Vo'] * info['Tiempo'],
        #Ecuación 3
        info['Altura'] - (1/2 * info['Gravedad']* (info['Tiempo']** 2))
      )
    )

    #Se añade una unidad(px) en el eje x.
    info['Distancia'] += 1
    
    #Se calcula el tiempo con la Ecuación 5.
    info['Tiempo'] = info['Distancia'] / info['Vo']
  
  #Retorna un directorio
  return info

#Recibe como parametro un directorio
def DibujarSemiParabolico(Simul):
  '''Creación de ventana gráfica'''
  
  #Crea la ventana gráfica con las medidas de la gráfica más 10px
  screen = GraphWin(
    Simul['Title'],
    Simul['Distancia'] + 10,
    Simul['Altura'] + 10
  )
  screen.setCoords(0, 0, Simul['Tiempo']* Simul['Vo'] + 10, Simul['Altura'] + 10)
  
  #Se crean los puntos el la ventana gráfica en relacion a los datos del directorio del parametro
  for x, y in Simul['Graphic']:
    c = Circle(Point(x, y), 0.5)
    c.setFill('blue')
    c.draw(screen)
  screen.getMouse()
  screen.close()


#lista de datos de prueba
DataPrueba = [
  {
    'name': 'Bala de cañon',
    'Vo': 100,
    'h': 400
  },
  {
    'name': 'Pelota',
    'Vo': 350,
    'h': 40
  },
  {
    'name': 'Dardo',
    'Vo': 530,
    'h': 12
  }
]

for Obj in DataPrueba:
  data = SimularSemiParabolico(Obj)
  DibujarSemiParabolico(data)