package mailSender;

import com.sendgrid.helpers.mail.Mail;
import com.sendgrid.helpers.mail.objects.Content;
import com.sendgrid.helpers.mail.objects.Email;
import mail.MailStrategy;
import mailCodes.MailCodes;
import mailInfo.MailInfo;
import com.sendgrid.*;

import java.io.IOException;


public class MailSender {

    private void sendGrid(String email, String text) throws IOException {
        Email from = new Email("nazar0620@gmail.com");
        String subject = "It works as you can see";
        Email to = new Email(email);
        Content content = new Content("text/plain", text);
        Mail mail = new Mail(from, subject, to, content);

        SendGrid sg = new SendGrid("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");
        Request request = new Request();
        try {
            request.setMethod(Method.POST);
            request.setEndpoint("mail/send");
            request.setBody(mail.build());
            Response response = sg.api(request);
            System.out.println(response.getStatusCode());
            System.out.println(response.getBody());
            System.out.println(response.getHeaders());
        } catch (IOException ex) {
            throw ex;
        }
    }

    public void sendMail(MailInfo mailInfo) throws IOException {
        String email = mailInfo.getClient().getMail();
        MailStrategy mailStrategyContent = MailCodes.mailCodes.get(mailInfo.getMailCode());
        String text = mailStrategyContent.generateText(mailInfo.getClient());
        System.out.println(email);
        this.sendGrid(email, text);

    }
}
