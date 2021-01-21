package mailBox;

import mailInfo.MailInfo;
import mailSender.MailSender;

import java.io.IOException;
import java.util.LinkedList;
import java.util.Queue;

public class MailBox {
    private final MailSender mailSender;
    Queue<MailInfo> infos = new LinkedList<>();

    public MailBox() {
        this.mailSender = new MailSender();
    }

    public void addMailInfo(MailInfo mailInfo) {
        infos.add(mailInfo);
    }

    public void sendAll() throws IOException {
        while (infos.size() > 0) {
            this.mailSender.sendMail(infos.remove());
        }
    }
}
