
public class Recursion_Practice {
  public static void main(String[] args) {
    String reversed = Main.PrintString("gravity is working against me");
    System.out.println(reversed);
    Main.word_counter(reversed);
  }

  public static String PrintString(String str) {
    String ret_string = "";
    if (str.length() == 0) {
      return ret_string;
    } else {
      ret_string = ret_string + str.charAt(str.length() - 1);
      return ret_string + PrintString(str.substring(0, str.length() - 1));
    }
  }

  public static void word_counter(String word) {
    int count = 1;
    for (int i = 0; i < word.length(); i++) {
      if (word.charAt(i) == ' ') {
        count++;
      }
    }
    System.out.println(count);
  }
  
}

