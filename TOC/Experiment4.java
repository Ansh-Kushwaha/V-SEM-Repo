import java.util.*;

class Experiment4 {
    public static void main(String[] args) {
        List<Character> symbols = new ArrayList<>(Arrays.asList('0', '1'));
        State q0 = new State(symbols);
        State q1 = new State(symbols);
        State q2 = new State(symbols);
        State q3 = new State(symbols);
        q0.transitions.put('0', q0);
        q0.transitions.put('1', q1);
        q1.transitions.put('0', q2);
        q1.transitions.put('1', q1);
        q2.transitions.put('0', q0);
        q2.transitions.put('1', q3);
        q3.transitions.put('0', q2);
        q3.transitions.put('1', q1);

        DFA end101 = new DFA(Arrays.asList(q0, q1, q2, q3), q0, Arrays.asList(q3));
        if (end101.check("110111"))
            System.out.println("Accepted");
        else System.out.println("Rejected");

        if (end101.check("1010101"))
            System.out.println("Accepted");
        else System.out.println("Rejected");
    }    
}