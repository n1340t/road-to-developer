public class Q4 {
  public static void main(String[] args) {
    int[] arr = { 100, 12, 11, 3, 5, 6 };
    recInsertionSort(arr, arr.length);
    for (int i = 0; i < arr.length; i++) {
      System.out.println(arr[i]);
    }
  }

  public static void recInsertionSort(int[] A, int n) {
    if (n <= 1) {
      return;
    }
    recInsertionSort(A, n - 1);
    int last = A[n - 1];
    int j = n - 2;
    while (j >= 0 && A[j] > last) {
      A[j + 1] = A[j];
      j--;
    }
    // System.out.println(n + " - " + j);
    A[j + 1] = last;
  }
  /* b) The time complexity of recursive algorithm is not better than the iterative version.
  Both iterative and recursive runs in time linear to n;
  */
}