package client;

import lombok.Getter;

public class Client {
    private static int current_id = 0;

    @Getter
    private final String name;
    @Getter
    private final int age;
    @Getter
    private final String sex;

    @Getter
    private final int id;
    @Getter
    private final String mail;

    public Client(String name, int age, String sex, String mail) {
        this.name = name;
        this.age = age;
        this.sex = sex;
        this.mail = mail;
        this.id = current_id++;
    }
}
