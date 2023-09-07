import java.util.*;

class Experiment3 {
    public static void main(String[] args) {
        List<Character> symbols = new ArrayList<>(Arrays.asList('0', '1'));
        State q0 = new State(symbols);
        State q1 = new State(symbols);
        State q2 = new State(symbols);
        State q3 = new State(symbols);
        q0.transitions.put('0', q0);
        q0.transitions.put('1', q1);
        q1.transitions.put('0', q0);
        q1.transitions.put('1', q2);
        q2.transitions.put('0', q0);
        q2.transitions.put('1', q3);
        q3.transitions.put('0', q3);
        q3.transitions.put('1', q3);

        DFA threeOne = new DFA(Arrays.asList(q0, q1, q2, q3), q0, Arrays.asList(q3));
        System.out.println(threeOne.check("11001010110101"));
    }    
}