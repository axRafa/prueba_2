class Mamifero:
    cantPatas = 4
    def __init__(self, mamas, esp_vida):
        self.cantMamas = mamas
        self.esperanzaDeVida = esp_vida

    def mamar(self):
        return 'El animalito esta mamando.'

    def nacer(self):
        return 'Un nuevo mamifero ha nacido!'

class AnimalMarino:
    def __init__(self, branquias, especie):
        self.tieneBranquias = branquias
        self.especie = especie
    
    def nadar(self):
        return 'El animal está nadando!'

class Cetaceo(Mamifero, AnimalMarino):
    # Noten que acá estoy agregando los valores mamas y esp_vida para
    # poder utilizarlos en super.
    def __init__(self, notas, vive_en, peso, mamas, esp_vida):
        self.notas = notas
        self.viveEn = vive_en
        self.peso = peso
        # Acá está el uso de super.
        # Esta función nos permite acceder a la clase padre Mamifero
        # para designarle a nuestro cetaceo los atributos cantMamas
        # y esperanzaDeVida
        super().__init__(mamas, esp_vida)

    def mamar(self):
        return 'Este animal no puede mamar'