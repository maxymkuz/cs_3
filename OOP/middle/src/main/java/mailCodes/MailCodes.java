package mailCodes;

import mail.AdvertisementStrategy;
import mail.HappyBirthdayStrategy;
import mail.MailStrategy;

import java.util.HashMap;
import java.util.Map;

public class MailCodes {
    public static Map<Integer, MailStrategy> mailCodes = new HashMap<Integer, MailStrategy>() {
        {
            put(1, new HappyBirthdayStrategy());
            put(2, new AdvertisementStrategy());
        }
    };
}
