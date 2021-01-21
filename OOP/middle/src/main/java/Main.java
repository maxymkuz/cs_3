import client.Client;
import mailBox.MailBox;
import mailInfo.MailInfo;

import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {
        Client client1 = new Client("Max", 18, "male", "kuzyshyn@ucu.edu.ua");
        Client client2 = new Client("Max", 18, "female", "maxymkuz@gmail.com");
        System.out.println(client1.getId());
        System.out.println(client2.getId());

        MailBox mailBox = new MailBox();
        mailBox.addMailInfo(new MailInfo(client1, 1));
        mailBox.addMailInfo(new MailInfo(client2, 2));
        mailBox.sendAll();
    }
}
