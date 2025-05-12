#include <iostream>
#include <string>
#include <ctime>

using namespace std;

// Класс отправления сообщений
class ToSendMessage {
private:
    string useremail;
    string receiveremail;
    string message;
public:
    string set_userEmail(const string& email) {
        useremail = email;
        return useremail;
    }
    string set_receiverEmail(const string& email) {
        receiveremail = email;
        return receiveremail;
    }
    string set_message(const string& msg) {
        message = msg;
        return message;
    }
};

// Проверить правильности email
bool check_emailValid(const string& email) {
    return (email.find('@') != string::npos) && (email.find('.') != string::npos);
}

// Получение имени пользователя из email
string get_usernameFromEmail(const string& email) {
    size_t pos = email.find('@');
    return (pos != string::npos) ? email.substr(0, pos) : "";
}

// Добавление имя отправителя в сообщение
string appendsender(const string& message, const string& senderemail) {
    string username = get_usernameFromEmail(senderemail);
    return message + " (от: " + username + ")";
}

// Добавление время к сообщению
string append_time(const string& message) {
    time_t now = time(nullptr);
    string result = message + "\nВремя отправки: " + string(ctime(&now));
    return result;
}

// Сообщение об успешной/неуспешной отправке
void print_status(bool sent) {
    if (sent)
        cout << "Письмо отправлено" << endl;
    else
        cout << "Письмо не отправлено" << endl;
}

int main() {
    ToSendMessage msg;

    cout << "Введите вашу электронную почту: ";
    string useremail;
    getline(cin, useremail);
    while (!check_emailValid(useremail)) {
        cout << "Некорректный email. Повторите ввод: ";
        getline(cin, useremail);
    }
    msg.set_userEmail(useremail);

    cout << "Введите электронную почту получателя: " << endl;
    string receiveremail;
    getline(cin, receiveremail);
    while (!check_emailValid(receiveremail)) {
        cout << "Некорректный email. Повторите ввод: " << endl;
        getline(cin, receiveremail);
    }
    msg.set_receiverEmail(receiveremail);

    bool status = (receiveremail == "kochkindv@vogu.ru");

    if (status) {
        cout << "Введите сообщение: " << endl;
        string message;
        getline(cin, message);
        msg.set_message(message);
        string outmsg = appendsender(msg.set_message(message), msg.set_userEmail(useremail));
        outmsg = append_time(outmsg);
        cout << "Ваше сообщение: " << outmsg << endl;
    }

    print_status(status);

    return 0;
}