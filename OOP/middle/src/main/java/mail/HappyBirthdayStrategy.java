package mail;

import client.Client;

public class HappyBirthdayStrategy extends MailStrategy {

    @Override
    public String generateText(Client client) {
        return "Dear " + Greetings.get(client.getSex()) +
                client.getName() + "! We congratulate " +
                "you with with your " + client.getAge() + "th birthday!";

    }
}
