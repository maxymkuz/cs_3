package mailInfo;

import client.Client;
import lombok.Getter;

public class MailInfo {
    @Getter
    private final Client client;
    @Getter
    private final int mailCode;

    public MailInfo(Client client, int mailCode) {
        this.client = client;
        this.mailCode = mailCode;
    }
}
