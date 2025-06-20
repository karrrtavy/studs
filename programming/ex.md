# Методичка к экзамену

## 1. Антипаттерны: Copy&Paste, спаггети-код

**Антипаттерн** — шаблон неэффективного решения задачи.

### Copy&Paste
- **Определение**: Создание кода с часто повторяющимися частями.
- **Последствия**:
  1. Дубликат кода усложняет восприятие программы и размножает ошибки из оригинала;
  2. Усложнение исправления ошибок, так как изменения нужно вносить во всех копиях.
- **Решение**:
  1. Код-ревью;
  2. Принцип DRY (Don't Repeat Yourself) — вынос общей логики в функции или классы;
  3. Рефакторинг.

**Пример антипаттерна**:
```cpp
int sumInt(const vector<int>& vec) {
    int sum = 0;
    for (int num : vec)
        sum += num;
    return sum;
}

double sumDouble(const vector<double>& vec) {
    double sum = 0.0;
    for (double num : vec)
        sum += num;
    return sum;
}

void main() {
    vector<int> intVec = {n values};
    vector<double> doubleVec = {n values};
    cout << "Sum int: " << sumInt(intVec) << endl;
    cout << "Sum double: " << sumDouble(doubleVec) << endl;
    return 0;
}
```
**Пример исправления**:
```cpp
template <typename T>
T sum(const vector<T>& vec) {
    T sum = T();
    for (const T& num : vec)
        sum += num;
    return sum;
}

void main() {
    vector<int> intVec = {n values};
    vector<double> doubleVec = {n values};
    cout << "Sum int: " << sum(intVec) << endl;
    cout << "Sum double: " << sum(doubleVec) << endl;
}
```
### Спаггети-код
- **Определение**: Сложный для понимания, слабо структурированный код.
- **Причины**:
  1. Множество связей (вложенные конструкции, goto, friend );
  2. Неявные зависимости.
- **Пример**:
```cpp
void f(int a, int b, int _x) {
    if (_x) {
        // another operation;
    } else {
        // another operation;
    }
}

void main() {
    f(1, 2, x);
    // something
    f(1, 2, x);
}
```

## 2. Антипаттерны. Магические числа, hard code, ненужная сложность 
### Магические числа
- **Определение**: Использование числовых констант в коде.
- **Пример**:
```cpp
int a = x * 8;
int b = c + 8;
float f = 34.593f;
float x = a * 34.6f;
```
- **Пример исправления**:
```cpp
const int NUM_ELEMENTS = 8;
const int NUM_BITS = 8;
const int ARRAY_SIZE = 10;
const float FVALUE = 34.59f;
// также можно использовать другой метод
const int NUM_BITS_INT = sizeof(int) * 8;
```
### Hard code
- **Определение**: Внедрение конкретных значений в код, вместо их вынесения в конфигурационные файлы, константы или базу данных.
- **Последствия**: усложнение поддержки и изменение программы.
- **Пример (условный)**:
```cpp
void connectToDB() {
    string host = "127.0.0.1";
    int port = 5432; //новость дня, postgres по умл предлагает вашу бд установить на этот порт
    string user = "admin";
    string password = "dayahuyznaet";
}

void main() {
    connectToDB();
}
```
-**Пример исправления** (смысл в выносе настроек в конфиг или иное окружение, а затем их подключить):
```cpp
// у нас например есть какое нибудь окружение, БД, есть метод getenv, который может обращаться к окружению
void connectToDatabase() {
    const char* host = getenv("DB_HOST");
    const char* portStr = getenv("DB_PORT");
    const char* user = getenv("DB_USER");
    const char* password = getenv("DB_PASS");
}

void main() {
    connectToDatabase();
} 
// смысл в том, чтобы данные не находились в исходниках
```
### Ненужная сложность (неоправданно универсальное решение)
- **Определение**: Намеренно усложненный код.
- **Причины**:
  1. Избыток абстракций, классов, паттернов;
  2. Ненужные уровни наследования;
  3. Гибкое решение там, где возможен простой код.
- **Пример**:
```cpp
// из проблем: 2 класса для простой проверки, виртуальный метод и динамическая память
class NumberValidator {
public:
    virtual bool validate(int) = 0;
    virtual ~NumberValidator() {}
};

class EvenNumberValidator : public NumberValidator {
public:
    bool validate(int num) override {
        return num % 2 == 0;
    }
};

void main() {
    NumberValidator* validator = new EvenNumberValidator();
    cout << validator->validate(4);
    delete validator;
}
```
- **Пример решения**:
```cpp
bool isEven(int num) {
    return num % 2 == 0;
}

void main() {
    cout << isEven(4);
}
```

## 3. Препроцессор-компилятор-компоновщик
- **Препроцессор** - программа для обработки текста. Он преобразует данные в соответствии с директивами препроцессора. Если данные не содержат директив препроцессора, то они остаются без изменений. Препроцессор может существовать как отдельная программа, так и быть интегрированным в компилятор.
- **Компилятор** - программа, которая переводит исходный код в инструкции процессора (как объектный файл, на схеме указано). При синтаксических ошибках объектный файл не создается.
- **Компоновщик** - на слэнге это линкер. Это программа, производящая линковку, сборку. Он принимает на вход один или несколько модулей и собирает по ним исполнимый модуль.

В общем, это этапы процесса трансляции исходника в виде текстового файла в представлении, которое может быть выполнено процессором.

**Сборка компоновщика**
Всем известно, что сборка программы происходит за счет другой специальной программы - компоновщика. 



![Схема](11.03.25/preproccessing_projects.drawio.png)