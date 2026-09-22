from math import gcd

class Fraction:
   """
   La classe Fraction représente un nombre rationnel.
   """
   
   def __init__(self, num, den):
      """
      Crée une nouvelle fraction à partir de son numérateur et
      de son dénominateur.

      Les fractions sont toujours réduites, et leur dénominateur
      sera toujours positif.
      """
      if den == 0:
         raise ZeroDivisionError("Le dénominateur ne peut pas être nul")

      if den < 0:
         self._den = -den
         self._num = -num
      else:
         self._den = den
         self._num = num

      self._réduction()

   def _réduction(self):
      """
      Méthode interne qui rend une fraction irréductible.
      """
      d = gcd(self._num, self._den)
      self._num = self._num // d
      self._den = self._den // d

   # On crée des fonctions pour lire les 2 attributs, 
   # mais pas de fonction pour les modifier: de ce fait
   # on s'assure que self._num et self._den ne seront pas
   # modifiés "à la main" depuis l'extérieur de notre objet.
   #
   # Ce n'est pas une garantie absolue, mais affiche clairement
   # notre intention que ces deux attributs ne devraient pas
   # être modifiés de la sorte.

   @property
   def num(self):
      if (self._num == 0):
         print("do something")
      return self._num

   @property
   def den(self):
      return self._den

   def __str__(self):
      """
      Renvoie une représentation de la fraction sous forme
      de chaîne de caractère, à destination des êtres humains.

      Cette fonction est automatiquement appelée par la syntaxe `str(<objet>)`. 
      Elle est notamment utilisée par défaut avec `print`.
      """
      if self._den == 1:
         return str(self.num)
      else:
         return "{}/{}".format(self._num, self._den)

   def __repr__(self):
      """
      La méthode magique __repr__ en python est censée retourner
      une chaîne de caractère représentant ce qu'il faudrait
      saisir en python pour recréer l'objet. Ce n'est pas 
      nécessairement la même chose que __str__.

      La méthode __repr__ est notamment utilisée lorsqu'on est en mode
      interactif, par exemple dans une boucle d'interaction python dans un terminal,
      ou bien avec jupyter lab.
      """

      return "Fraction({},{})".format(self._num, self._den)

   def __eq__(self, q):
      """
      Renvoie True ssi self == q (mathématiquement)
      """
      return self._num*q._den == self._den*q._num

   def __lt__(self, q):
      """
      Renvoie True ssi self < q
      """

      dénominateur_commun = self._den * q._den
      if dénominateur_commun > 0:
         return self._num*q._den < q._num*self._den
      else:
         return self._num*q._den > q._num*self._den

   def __le__(self, q):
      """
      Renvoie True ssi self <= q
      """

      dénominateur_commun = self._den * q._den
      if dénominateur_commun > 0:
         return self._num*q._den <= q._num*self._den
      else:
         return self._num*q._den >= q._num*self._den

   def __add__(self, q):
      """
      Renvoie une nouvelle fraction correspondant à self+q
      """
      return Fraction(self._num*q._den + q._num*self._den, self._den*q._den)

   def __sub__(self, q):
      """
      Renvoie une nouvelle fraction correspondant à self-q
      """
      return Fraction(self._num*q._den - q._num*self._den, self._den*q._den)

   def __mul__(self, q):
      """
      Renvoie une nouvelle fraction correspondant à self*q
      """
      return Fraction(self._num*q._num, self._den*q._den)

   def __truediv__(self, q):
      """
      Renvoie une nouvelle fraction correspondant à self/q
      Peut déclencher une exception de division par zéro.
      """
      return Fraction(self._num*q._den, self._den*q._num)

   def __neg__(self):
      """
      Renvoie une nouvelle fraction correspondant à -self
      """
      return Fraction(-self._num, self._den)

   def __float__(self):
      """
      Renvoie une valeur approchée de self
      """

      return self._num / self._den