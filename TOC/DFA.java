import java.util.*;

public class DFA {
    List<State> states;
    List<State> finalSt;
    State initial;

    public DFA(List<State> states, State initial, List<State> finalSt) {
        this.states = states;
        this.initial = initial;
        this.finalSt = finalSt;
    }

    public boolean check(String s) {
        State curr = initial;
        for (char ch : s.toCharArray()) {
            if (curr.symbols.contains(ch)) {
                curr = curr.transitions.get(ch);
            }
            else
                return false;
        }

        if (finalSt.contains(curr))
            return true;
        return false;
    }
}