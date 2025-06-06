import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.util.Random;

public class Eid_wish extends JPanel implements ActionListener{
    private String message = "✨ Eid Mubarak! May your life be full of joy and blessings! 🌙";
    private int x = -800;
    private Timer timer;
    private Image bgi;
    private Random read = new Random();
    private Color[] fireworkColors = {Color.YELLOW, Color.CYAN, Color.MAGENTA,Color.ORANGE,};

    public Eid_wish(){
        setBackground(Color.BLACK);
        setForeground(Color.GREEN);
        setFont(new Font("Serif", Font.ITALIC,27));

        bgi = Toolkit.getDefaultToolkit().getImage("ChatGPT Image Jun 4, 2025, 01_56_03 AM.png");

        timer = new Timer(50,this);
        timer.start();
    }

    @Override
    protected void paintComponent(Graphics g){
        super.paintComponent(g);

        g.drawImage(bgi,0,0,getWidth(),getHeight(),this);

        g.setColor(getForeground());
        g.setFont(getFont());
        g.drawString(message,x,getHeight()/2);

        drawfireworks(g);
    }

    private void drawfireworks(Graphics g){
        for (int i =0;i<15;i++);{
            int fx = read.nextInt(getWidth());
            int fy = read.nextInt(getHeight()/2);
            int fsize = 10 +read.nextInt(20);

            g.setColor(fireworkColors[read.nextInt(fireworkColors.length)]);
            g.fillOval(fx, fy, fsize, fsize);
        }
    }

    @Override
    public void actionPerformed(ActionEvent e){
        x+=4;
        if (x>getWidth())x = -message.length()*10;
        repaint();
    }

    public static void main(String[] args){
        MusicPlayer.play("Eid mubarak - 1.wav");

        JFrame frame = new JFrame("Eid Wish");
        frame.setSize(1280,720);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setLocationRelativeTo(null);

        Eid_wish animationPanel = new Eid_wish();
        frame.add(animationPanel);

        frame.setVisible(true);
    }
}