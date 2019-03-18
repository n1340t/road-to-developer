public class Q5 {
  public static void main(String[] args) {
    String str = "123ana321";
    System.out.println(isPalindrome2(str));
  }

  // Q5 B
  public static boolean isPalindrome2(String s) {
    int i = 0;
    int j = s.length() - 1;
    return isPalindromeRec(s, i, j);
  }

  public static boolean isPalindromeRec(String s, int i, int j) {
    System.out.println(i + " -- " + j);
    if (i != j && i < Math.ceil(s.length() / 2) && s.charAt(i) == s.charAt(j)) {
      i++;
      j--;
      return isPalindromeRec(s, i, j);
    } else {
      return i == j;
    }
  }

  // Q5 A
  public static boolean isPalindrome(String s) {
    int i = 0, j = s.length() - 1;
    System.out.println(Math.ceil((s.length() / 2)));
    while (i != j && i < Math.ceil(s.length() / 2) && s.charAt(i) == s.charAt(j)) {
      i++;
      j--;
    }
    return i == j;
  }
}