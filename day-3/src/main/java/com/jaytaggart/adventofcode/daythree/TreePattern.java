package com.jaytaggart.adventofcode.daythree;

public class TreePattern {
    private String pattern;

    public TreePattern(String pattern) {
        this.pattern = pattern;
    }

    public String getPattern() {
        return pattern;
    }

    public void extendPattern() {
        this.pattern = this.pattern + this.pattern;
    }

    public static TreePattern fromString(String s) {
        return new TreePattern(s);
    }
}
