import java.util.*;

public class DFA {
    List<State> states;
    State initial;

    public DFA(List<State> states, State initial, List<State> finalSt) {
        this.states = states;
        this.initial = initial;
        this.initial.isInitial = true;
        for (State f : finalSt)
            f.isFinal = true;
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

        if (curr.isFinal)
            return true;
        return false;
    }
}