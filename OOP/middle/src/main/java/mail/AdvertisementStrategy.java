package mail;

import client.Client;

public class AdvertisementStrategy extends MailStrategy {
    @Override
    public String generateText(Client client) {
        return "Dear " + Greetings.get(client.getSex()) +
                client.getName() + "! Want to notify you that we have some new products" +
                " with a low price available. Go check them out;";
    }
}
