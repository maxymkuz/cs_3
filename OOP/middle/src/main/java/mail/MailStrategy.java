package mail;

import client.Client;

import java.util.HashMap;
import java.util.Map;

public abstract class MailStrategy {
    protected Map<String, String> Greetings = new HashMap<String, String>() {
        {
            put("male", "Mr.");
            put("female", "Mrs.");
        }
    };

    public abstract String generateText(Client client);
}
