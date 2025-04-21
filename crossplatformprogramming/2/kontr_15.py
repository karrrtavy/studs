class ShapeExpertSystem:
    def __init__(self):
        self.shape = None
        self.questions = {
            "circle": "Загадана ли круглая фигура?",
            "rectangle": "Четырехугольная фигура с прямыми углами?",
            "triangle": "Представляет ли фигура собой треугольник?"
        }

    def ask_question(self, question):
        response = input(question + " (да/нет): ").strip().lower()
        return response == "да"

    def determine_shape(self):
        for shape, question in self.questions.items():
            if self.ask_question(question):
                self.shape = shape
                break

    def calculate_area(self):
        if self.shape == "circle":
            radius = float(input("Введите радиус круга: "))
            area = 3.14159 * (radius ** 2)
        
        elif self.shape == "rectangle":
            width = float(input("Введите ширину прямоугольника: "))
            height = float(input("Введите высоту прямоугольника: "))
            area = width * height
        
        elif self.shape == "triangle":
            base = float(input("Введите основание треугольника: "))
            height = float(input("Введите высоту треугольника: "))
            area = 0.5 * base * height
        
        else:
            print("Не удалось определить фигуру.")
            return None
        
        return area

def main():
    expert_system = ShapeExpertSystem()
    expert_system.determine_shape()
    area = expert_system.calculate_area()

    if area is not None:
        print(f"Площадь фигуры: {area}")

if __name__ == "__main__":
    main()
