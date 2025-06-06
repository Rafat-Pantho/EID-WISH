import javax.sound.sampled.*;

public class MusicPlayer {
    public static void play(String path) {
        try {
            AudioInputStream audioStream = AudioSystem.getAudioInputStream(new java.io.File(path));
            Clip clip = AudioSystem.getClip();
            clip.open(audioStream);
            clip.loop(Clip.LOOP_CONTINUOUSLY);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}