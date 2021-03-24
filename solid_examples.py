## Exemplo incorreto de uso de classes segundo o método SOLID
## S - Single Responsability
## Classes devem possuir apenas uma responsabilidade em um determinado contexto,
## a classe abaixo é responsável por retornar dados de uma conta bancária e salvar estes no banco de dados da aplicação
class Account:
   ''' Classe de Demonstraçao de Principios SOLID''''
   def __init__(self, account_no: str): ## inicializaçao de atributos
       self.account_no = account_no

   def get_account_number(self):        ## getters da funçao
       return self.account_no

   def save(self):                      ## metodo para salvar dados de uma conta no banco de dados
     pass

## Correção:
## Uso de classes com propósito único, assim 
## Esta classe é responsável pelo salvamento de dados de classes no banco de dados
class AccountDB:
   def get_account_number(self, _id):   ## getter para recepção de dados do numero da conta
       pass

   def account_save(self, obj):         ## método que realiza o salvamento de dados da conta no banco de dados 
       pass

## Classe Conta reúne dados de uma conta fictícia
class Account:
   def __init__(self, account_no: str): ## incialização de atributos
       self.account_no = account_no
       self._db = AccountDB()           ## referencia da Classe AccountDB para uso de atributos e métodos nesta classe
       
   def get_account_number(self):        ## método getter
       return self.account_no

   def get(self, _id):                  ## retorno de paramentros do método get_account_number() da classe AcountDB
       return self._db.get_account_number(_id=_id)

   def save(self):                      ## salvamento de dados realizado pelo método account_save da classe AcountDB
       self._db.account_save(obj=self)


## Exemplo incorreto de uso de classes segundo o método SOLID
## O - Open and Close Principle
## Classes, funçoes e métodos são passiveis a extensão, porém, não a modificação
## Esta classe logo abaixo realiza descontos em preços de uma determinada loja 
class Discount:
   def __init__(self, customer, price): ## incilizaçao de atributos
       self.customer = customer
       self.price = price

   def give_discount(self):             ## método para distribuição de a descontos
       if self.customer == 'normal':
           return self.price * 0.2
       elif self.customer == 'vip':
           return self.price * 0.4
    ## Porém, ao limitar o poder de realizaçao de descontos a este método tal classe está passivel a mudanças em sua estrutura de código:
    ## EX:
    ## cliente vip comprou uma grande quantidade de produtos e requisita um desconto maior:
    ## isso automáticamente implica em uma mudança na estrutura acima, oque viola diretamente o pricípio abordado neste tópico

## Correção: 
## estender o uso do método em diferentes classes:
class Discount:
   def __init__(self, customer, price): ## incialização de atributos
       self.customer = customer
       self.price = price
   def get_discount(self):              ## método para dar descontos
       return self.price * 0.2

class VIPDiscount(Discount):        ## classe VIPDiscount está herdando atributos e métodos da classe Discount
   def get_discount(self): ## método para dar descontos, está estendendo métodos da classe mãe para tal
       return super().get_discount() * 2

class SuperVIPDiscount(VIPDiscount): ## classe está herdando atributos e métodos da classe VIPDiscount
   def get_discount(self):  ## método para dar descontos, está estendendo métodos da classe mãe para tal
       return super().get_discount() * 2

## Exemplo incorreto de uso de classes segundo o método SOLID
## L - Pricípio da Subistuição de Liskov (em ingles - Liskov Subistitution Principle - LSP)
## Este princípio enuncia que dada uma classe F(x) que contenham definiçoes sobre objetos x de um determinado conjunto T,
## classes do tipo F(y) que contenham definiçoes sobre objetos y de um determinado conjunto S, sendo S um subconjunto de T,
## podem substituir as primeiras funçoes, sem causar danos ao programa
class Vehicle:
   def __init__(self, name: str, speed: float): ## inicialização de atributos da classe
       self.name = name
       self.speed = speed

   def get_name(self) -> str:   # método retorna o nome do veiculo
       return f"The vehicle name {self.name}"

   def get_speed(self) -> str:  ## método retorna a velocidade do veiculo
       return f"The vehicle speed {self.speed}"

   def engine(self):        ## método sobre motores do veiculo
       pass

   def start_engine(self):  ## método para ligar o veículo
       self.engine()


class Car(Vehicle):         ## Classe Carro herda atributos e métdos da classe Vehicle
   def start_engine(self):  ## método para ligar o carro
       pass


class Bicycle(Vehicle):     ## Classe bicicleta herda atributos e métodos da classe Vehicle
   def start_engine(self):  ## método para "ligar" a bicicleta
       pass
            ## Neste ponto do código observa-se um erro lógico quanto o uso de classes:
            ## um veiculo bicicleta não possui motores, assim, não há motores a serem ligados

## Correção:
## Uma correção plausível para tal código é a criação de métodos para diferentes casos possíveis
class Vehicle:
   def __init__(self, name: str, speed: float):## inicialização de atributos da classe Vehicle
       self.name = name
       self.speed = speed

   def get_name(self) -> str:                   ## método retorna o nome do veiculo
       return f"The vehicle name {self.name}"

   def get_speed(self) -> str:                  ## método retorna a velocidade do veiculo
       return f"The vehicle speed {self.speed}"

class VehicleWithoutEngine(Vehicle):            ## classe herda atributos e métodos da classe Vehicle, para veiculos sem motores
   def start_moving(self):                      ## método inicializa o movimento do veiculo
      raise NotImplemented

class VehicleWithEngine(Vehicle):           ## classe refere-se a Veiculos que possuam Motores, herda atributos da classe Veiculo
   def engine(self):                        ## método para descrição de motores do veiculo
      pass
   def start_engine(self):                  ## método para ignição de motores do veiculo
      self.engine()

class Car(VehicleWithEngine):                ## Classe CAR herda atributos e métodos da classe Vehicle
   def start_engine(self):
       pass

class Bicycle(VehicleWithoutEngine):         ## Classe Bicycle herda atributos e métodos da classe Vehicle
   def start_moving(self):
       pass 

## Exemplo incorreto de uso de classes segundo o método SOLID
## I - Pricípio da Segregação de Interfaces (em ingles - Interface Segregation Principle - LSP)
## Este princípio sugere que classes que não serão utilizadas não devem ser chamadas
class Shape:                ## classe forma  de objeto
   def draw_circle(self):   ## método para desenhar um circulo
       raise NotImplemented

   def draw_square(self):   ## método para desenhar um quadrado
       """ Draw a square"""
       raise NotImplemented

class Circle(Shape):        ## classe Circle herda atributos e métodos da classe Shape

   def draw_circle(self):   ## método para desenhar um círculo
       """Draw a circle"""
       pass

   def draw_square(self):   ## método para desenhar um quadrado
       """ Draw a square"""
       pass
                            ## neste último método observa-se a utilização do método para desenhar quadrados, contudo,
                            ## tal método é desnecessário para esta classe, tendo em vista, que esta relaciona-se apenas
                            ## a contruçao de círculos

## Correção:
## Uma correção plausível para tal código é a retirada de métodos desnecessários para a classe
class Shape:                ## classe para desenhar formas de objetos
   def draw(self):          ## método desenhar
      """Draw a shape"""
      raise NotImplemented

class Circle(Shape):        ## classe circulo, herda atributos da classe Forma
   def draw(self):          ## método para desenhar círculos
      """Draw a circle"""
      pass

class Square(Shape):        ## classe quadrado, herda atributos da classe Forma
   def draw(self):          ## método para desenhar quadrados
      """Draw a square"""
      pass

## Exemplo incorreto de uso de classes segundo o método SOLID
## D - Pricípio da Inversão de Dependencias
## 1 - Este princípio enuncia que módulos de alto nível nao podem depender de módulos de baixo nível, ambos devem depender de abstraçoes
## 2 - Abstraçoes nao devem depender de detalhes, detalhes devem depender de abstraçoes
class BackendDeveloper:## módulo de baixo nível
    @staticmethod
    def python():
        print("Writing Python code")

class FrontendDeveloper:## módulo de baixo nível
    @staticmethod
    def javascript():
        print("Writing JavaScript code")

class Project:          ## módulo de alto nivel

    def __init__(self): ## inicializaçao de atributos
                        ## chamada das classes previamente declaradas por meio destes dois atrbutos
        self.backend = BackendDeveloper() 
        self.frontend = FrontendDeveloper()

    def develop(self):  ## método da classe
        self.backend.python()
        self.frontend.javascript()
        return "Develop codebase"

## instanciação de classe
project = Project()
print(project.develop())    

## Correçao:
class BackendDeveloper:## Módulo de baixo nível
   def develop(self):
       self.__python_code()
   
   @staticmethod
   def __python_code():
       print("Writing Python code")

class FrontendDeveloper:## Módulo de baixo nível
   def develop(self):   
       self.__javascript()
   
   @staticmethod
   def __javascript():
       print("Writing JavaScript code")

class Developers:   ## Módulo abstrato
   def __init__(self):  ## inicialização de atributos
       self.backend = BackendDeveloper()
       self.frontend = FrontendDeveloper()

   def develop(self):   ## método desenvolver
       self.backend.develop()
       self.frontend.develop()

class Project:      ## Módulo de alto nível
   def __init__(self):
       self.__developers = Developers()     ## importação do módulo abstrato

   def develops(self):
       return self.__developers.develop()

##instanciaçao de classe
project = Project()
print(project.develops())
