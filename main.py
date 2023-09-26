from typing import List

#Elemental masses collected from ptable.com
#-----------------------------------------------------------------------------------------
indxSym = ["H","He","Li","Be","B","C","N","O","F","Ne","Na","Mg","Al","Si","P","S","Cl","Ar","K","Ca",
"Sc","Ti","V","Cr","Mn","Fe","Co","Ni","Cu","Zn","Ga","Ge","As","Se","Br","Kr","Rb","Sr","Y","Zr","Nb",
"Mo","Tc","Ru","Rh","Pd","Ag","Cd","In","Sn","Sb","Te","I","Xe","Cs","Ba","La","Ce","Pr","Nd","Pm","Sm",
"Eu","Gd","Tb","Dy","Ho","Er","Tm","Yb","Lu","Hf","Ta","W","Re","Os","Ir","Pt","Au","Hg","Tl","Pb","Bi",
"Po","At","Rn","Fr","Ra","Ac","Th","Pa","U","Np","Pu","Am","Cm","Bk","Cf","Es","Fm","Md","No","Lr","Rf",
"Db","Sg","Bh","Hs","Mt","Ds","Rg","Cn","Nh","Fl","Mc","Lv","Ts","Og"]
#Index of all elemental symbols
indxMM = [1.008, 4.0026, 6.94, 9.0122, 10.81, 12.011, 14.007, 15.999, 18.998, 20.180, 22.99, 24.305,
26.982, 28.085, 30.974, 32.06, 35.45, 39.948, 39.098, 40.078, 44.956, 47.867, 50.942, 51.996, 54.938,
55.845, 58.933, 58.693, 63.546, 65.38, 69.723, 72.630, 74.922, 78.971, 79.904, 83.798, 85.468, 87.62,
88.906, 91.224, 92.906, 95.95, 98, 101.07, 102.91, 106.42, 107.87, 112.41, 114.82, 118.71,
102.76, 127.6, 126.9, 131.29, 132.91, 137.33, 138.91, 140.12, 140.91, 144.24, 145, 150.36, 151.96,
157.25, 158.93, 162.5, 164.93, 167.26, 168.93, 173.05, 174.97, 178.49, 180.95, 183.84, 186.21, 190.23,
192.22, 195.08, 196.97, 200.59, 204.38, 207.2, 208.98, 209, 210, 222, 223, 226, 227, 232.04, 231.04,
238.03, 237, 244, 243, 247, 247, 251, 252, 257, 258, 259, 266, 267, 268, 269, 270, 270, 278, 281,
282, 285, 286, 289, 290, 293, 294, 294]
#Index of all Elemental masses (From ptable.com)


#-----------------------------------------------------------------------------------------


#Cohesive parent function
def findTotalMass(formString):
    if (formString.strip()) and (type(formString) == str):
        baseList = breakStr(formString)
        ANum,Amt = splitList(baseList)
    
        MolMas = []
        for i in range(len(ANum)):
            MolMas.append(indxMM[ANum[i]])
        TMM = 0
        for i in range(len(ANum)):
            TMM = TMM + (MolMas[i]*Amt[i])
            return TMM
    else:
        return None


#Function to deconstruct the original string into a list
def breakStr(string):
  m_list = []
  #Ords 48 - 57 = chars 0 - 9; Ords 65 - 90 = chars A - Z; Ords 97 - 122 = chars a - z
  for i in range(len(string)):
    if (ord(string[i]) <= 90 ) and (ord(string[i]) >= 65): #Check if Capital letter
      if(ord(string[i+1]) <= 122) and (ord(string[i+1]) >= 97): #Check if lowercase letter
        m_list.append(string[i]+string[i+1]) #Append Both letters to list
        if (ord(string[i+2]) <= 57) and (ord(string[i+2]) >= 48): #Check if number
          if (ord(string[i+3]) <= 57) and (ord(string[i+3]) >= 48): #Check if number
            m_list.append(string[i+2]+string[i+3])
          else:
            m_list.append(string[i+2])
        else:
          m_list.append("1")
      elif (ord(string[i+1]) <= 57) and (ord(string[i+1]) >= 48): #Check if number
        m_list.append(string[i])
        if (ord(string[i+2]) <= 57) and (ord(string[i+2]) >= 48): #Check if number
          m_list.append(string[i+1]+string[i+2])
        else:
          m_list.append(string[i+1])
      else:
        m_list.append(string[i])
        m_list.append("1")
  return m_list

#Splits baseList into the Symbol indexes and the amount of each
def splitList(baseList):
  listA: List[int] = []
  listB: List[int] = []
  for i in range(len(baseList)):
    if i % 2 == 0:
      listA.append(indxSym.index(baseList[i]))
    else:
      listB.append(int(baseList[i]))
  return listA,listB

#Main Loop
print("WARNING: Only works with amounts of individual elements less than 100")
while True:
  formString = input("Formula: ") + " "
  mm = findTotalMass(formString)
  if mm == None:
    print("ValueError: You need to input a formula, not a blank space.")
  else:
    print(str(mm) + f"g/mol of {formString}\n")