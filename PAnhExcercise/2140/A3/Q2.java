public class Q2 {
  public static void main(String[] args) {
    System.out.println("Helllllo");
    LinkedList shifts = new LinkedList();
    shifts.insert(1);
    shifts.insert(2);
    shifts.insert(15);
    shifts.insert(14);
    shifts.insert(23);
    shifts.insert(25);
    // shifts.printList();
    CircularLinkedList circularList = new CircularLinkedList();
    Node currentNode = shifts.head;
    while (currentNode != null) {
      if (currentNode.getValue() % 2 == 1) {
        circularList.insert(currentNode.getValue());
      }
      currentNode = currentNode.getNext();
    }
    circularList.transform();
    String[] circularArray = giveShifts(circularList);
    for(int i = 0; i < circularArray.length; i++) {
      System.out.println(i + " > " + circularArray[i]);
    }
  }

  public static String[] giveShifts(CircularLinkedList list) {
    String[] circular;
    int length = list.getListLength();
    Node currentNode = list.head;
    if (length > 0) {
      circular = new String[length];
      while (length > 0) {
        length--;
        circular[length] = list.getCircular(currentNode);
        currentNode = currentNode.getNext();
      }
    } else {
      circular = new String[1];
    }
    return circular;
  }
}

class CircularLinkedList {
  protected Node head;

  public CircularLinkedList() {
    head = null;
  }

  public void insert(int newValue) {
    head = new Node(newValue, head);
  }

  public void transform() {
    Node currentNode = head;
    while (currentNode.getNext() != head) {
      if (currentNode.getNext() != null) {
        currentNode = currentNode.getNext();
      } else {
        currentNode.setNext(head);
      }
    }
  }

  public void printList() {
    Node currentNode = head;
    do {
      System.out.print(currentNode.getValue() + ", ");
      currentNode = currentNode.getNext();
    } while (currentNode.getValue() != head.getValue());
  }

  public String getCircular(Node positionHead) {
    Node currentNode = positionHead;
    String str = "";
    do {
      str += currentNode.getValue() + ", ";
      currentNode = currentNode.getNext();
    } while (currentNode.getValue() != positionHead.getValue());
    return str.replaceAll(", $", "");
  }

  public int getListLength() {
    Node currentNode = head;
    int length = 0;
    do {
      length += 1;
      currentNode = currentNode.getNext();
    } while (currentNode.getValue() != head.getValue());
    return length;
  }
}

class LinkedList {
  protected Node head;

  public LinkedList() {
    head = null;
  }

  public void insert(int newValue) {
    head = new Node(newValue, head);
  }

  public void printList() {
    Node currentNode = head;
    while (currentNode != null) {
      System.out.print(currentNode.getValue() + ", ");
      currentNode = currentNode.getNext();
    }
  }
}

class Node {
  protected int value;
  protected Node next;

  public Node(int newValue, Node newNext) {
    value = newValue;
    next = newNext;
  }

  public Node(int newValue) {
    this(newValue, null);
  }

  public int getValue() {
    return value;
  }

  public void setValue(int newValue) {
    value = newValue;
  }

  public Node getNext() {
    return next;
  }

  public void setNext(Node newNext) {
    next = newNext;
  }
}