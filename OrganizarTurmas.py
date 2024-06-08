import prettytable as prettytable
import random as rnd
POPULATIO_SIZE=9
NUMBER_OF_ELITE_SCHEDULES=1
TOURNAMENT_SELECTION_SIZE=4
MUTATION_RATE=0.25
class Informacoes:
    Salas=[["S1",85],["S2",90],["S3",120]]
    HoradasAulas=[["HA1", "PP 14:30 - 16:00"],
                  ["HA2","PP 16:20 - 18:00"],
                  ["HA3","SP 14:30 - 16:00"],
                  ["HA4","SP 16:30 - 18:00"]]
    Professores=[["P1", "Raimundo"],
                 ["P2", "José Freitas"],
                 ["P3", "Francisco"],
                 ["P4", "Nayara"]]
    
def __init__(self):
    self._salas=[];self._horadasaulas=[]; self._professores[]
    for i in range (0,len(self.Salas)):
        self._salas.append(Sala(self.Salas[i][0],self.Salas[i][1]))
    for i in range (0,len(self.HoradasAulas)):
        self._horadasaulas.append(HoradaAula(self.HoradasAulas[i][0],self.HoradasAulas[i][1]))
    for i in range (0,len(self.Salas)):
        self._professores.append(Professor(self.Professores[i][0],self.Professores[i][1]))
    materia1= Materia(1,"Matématica Discreata",[self._professores[0]],36)
    materia2= Materia(2,"Inteligência Artificial",[self._professores[1]],45)
    materia3= Materia(3,"Banco de Dados",[self._professores[0]],34)
    materia4= Materia(4,"Segurança da Informaçção",[self._professores[2]],36)
    materia5= Materia(5,"Calculo",[self._professores[3]],45)
    materia6= Materia(6,"Estágio Curricular",[self._professores[4]],44)
    materia7= Materia(7,"Teste de Coclusãode Curso",[self._professores[3]],45)
    self._materias=[materia1,materia2,materia3,materia4,materia5,materia6,materia7]
    hora1=Horario("5 periodo",[materia1, materia2,materia4,materia5])
    hora2=Horario("6 periodo",[materia3,materia6,materia5])
    hora3=Horario("7 periodo",[materia7,materia4])
    self._horarios=[hora1,hora2,hora3]
    self._numerodeclasses=0
    for i in range(0,len(self._horarios)):
        self._numerodeclasses += len(self._horarios[i].get_materia())
    def get_salas(self): return self._salas
    def get_professores(self): return self._professores
    def get_materias(self): return self._materias
    def get_horarios(self): return self._horarios
    def get_horadasaulas(self): return self._horadasaulas
    def get_numerodeclasses(self): return self._numerodeclasses

class Schedule:
    def __init__(self):
        self._Informacoes=Informacoes 
        self._horarios= []
        self._numeroDeConflitos= 0
        self._fitness=-1
        self._classNumb=0
        self._isFitnessChanged=True
    def get_horarios(self):
        self._isFitnessChanged=True
        return self._horarios
    def get_numeroDeConflitos(self): return self._numeroDeConflitos
    def get_fitnss(self): 
        if (self.isFitnessChanged==True):
            self._fitness=self.calculate_fitness()
            self._isFitnessChanged=False
        return self._fitness
    def initialize(self):
        profundidade=self._informacoes.getprofundidade()
        for i in range (0, len(profundidade)):
            materia=profundidade[i].get_materia()
            for j in range (0, len(materia)):
                newHorario = Horario(self._classnNumb, profundidade[i], materia[j])
                self._classNumb+=1
                newHorario.setHoradaAula(Informacoes.HoradaAula()[rnd.randrange(0,len(Informacoes.get_HoradaAula()))])
                newHorario.set_Sala(Informacoes.get_Sala()[rnd.randrange(0,len(Informacoes.get_Sala()))])
                newHorario.set_Professor(Informacoes.get_Professor()[rnd.randrange(0,len(Informacoes.get_Professor()))])
                self._horarios.apend(newHorario)
        return self
    def calculate_fitness(self):
        self._numeroDeConflitos=0
        horarios=self.get_classes()
        for i in range(0,len(horarios)):
            if (horarios[i].get_sala().get_capacidade() < horarios[i].get_materia().get_MaxnumberOfstudents()):
                self._numeroDeConflitos+=1
            for j in range(0,len(horarios)):
                if(j>=i):
                    if (horarios[i].get_horadaaula()== horarios[j].get_horadaaula() and horarios[i].get_id() !=horarios[j].get_id()):
                        if (horarios[i].get_Sala == horarios[j].get_sala()):self._numeroDeConflitos+=1
                        if (horarios[i].get_Professor == horarios[j].get_sala()):self._numeroDeConflitos+=1
        return 1/((1.0*self._numeroDeConflitos + 1))
    def __str__(self):
        returnValue="" 
        for i in range (0,len(self._horarios)-1):
            returnValue+=str(self._horarios[i])+","
        returnValue+= str(self._horarios[len(self._horarios)-1])
        return returnValue
        
class Populacao:
    .... ....

class AlgoritimoGenetico:
    ... ...

class Materia:
    def __init__(self,number,name,instructor,MaxnumberOfstudents):
        self.number=number
        self.name=name
        self.instructor=instructor
        self.MaxnumberOfstudents=MaxnumberOfstudents 
    def get_number(self): return self.get_number
    def get_name(self): return self.get_name
    def get_instructor(self): return self.get_instructor
    def get_MaxnumberOfstudents(self): return self.get_MaxnumberOfstudents
    def __str__(self): return self._name
class Professor:
    def __init__(self,id, name):
        self._id=id
        self._name=name
    def get_id(self): return self.get_id
    def get_name(self): return self.get_name
    def __str__(self): return self._name

class Sala:
    def __init__(self,numero, capacidade):
        self._numero=numero
        self._capacidade=capacidade
    def get_numero(self): return self.get_numero
    def get_capacidade(self): return self.get_capacidade

class HoradaAula:
    def __init__(self,id, hora):
        self._id=id
        self._hora=hora
    def get_id(self): return self.get_id
    def get_hora(self): return self.get_hora

class Periodo:
    def __init__(self,name,materias):
        self._name=name
        self._materias=materias 
    def get_name(self): return self._name 
    def get_materias(self): return self._materias 
    
class Horario:
    def __init__(self,id, periodo,materia):
        self._id=id
        self._periodo=periodo
        self._materia=materia
        self._professor=None
        self._horadaaula=None
        self._sala=None
    def get_id(self): return self.get_id
    def get_periodo(self): return self.get_periodo
    def get_materia(self): return self.get_materia
    def get_professor(self): return self.get_professor
    def get_horadaaula(self): return self.get_horadaaula
    def get_sala(self): return self.get_sala
    def set_professor(self, professor):self._professor=professor
    def set_horadaaula(self,horadaaula):self._horadaaula=horadaaula
    def set_sala(self,sala):self._sala=sala
    def __str__(self):
        return str(self._periodo.get_name())+ "," + str(self._materia.get_number()) + "," + str(self._sala.get_numero())+ "," + str(self._professor.get_id()) + "," + str(self._horadaaula.getide())
    
informacao=Informacoes()
