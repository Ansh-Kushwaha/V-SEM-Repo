public class DFA {
    List<State> states;
    State initial;

    public DFA(List<State> states, State initial, List<State> finalS) {
        this.states = states,
        this.initial = initial;
        this.initial.setInitial();
        for (State f : finalSt)
            f.setFinal();
    }

    public boolean check(String s) {
        State curr = initial;
        for (char ch : s.toCharArray()) {
            if (curr.symbols.contains(ch)) {
                curr = curr.transitions.get(ch);
            }
        }

        if (finalS.contains(curr))
            return true;
        return false;
    }
}