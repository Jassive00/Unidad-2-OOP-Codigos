class libro:
    def __init__(self, titulo, num_paginas):
        self.titulo = titulo
        self.num_paginas = num_paginas

    def __str__(self):
        return f"Libro: {self.titulo}, Páginas: {self.num_paginas}"

    def __len__(self):
        return self.num_paginas

libro1 = libro("Cien años de soledad", 471)
print(libro1)
print("Número de páginas:", len(libro1))