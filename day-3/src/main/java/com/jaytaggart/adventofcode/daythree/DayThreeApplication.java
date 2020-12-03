package com.jaytaggart.adventofcode.daythree;

import java.io.File;
import java.io.IOException;
import java.net.URI;
import java.net.URISyntaxException;
import java.nio.file.Files;
import java.util.List;
import java.util.Objects;
import java.util.stream.Collectors;

public class DayThreeApplication {
    public static void main(String[] args) throws IOException, URISyntaxException {
        List<TreePattern> input = getInput();
        input.stream().map(TreePattern::getPattern).forEach(System.out::println);
    }

    private static List<TreePattern> getInput() throws URISyntaxException, IOException {
        URI inputResource = Objects.requireNonNull(DayThreeApplication.class.getClassLoader().getResource("input.txt"))
                                   .toURI();
        File inputFile = new File(inputResource);
        return Files.readAllLines(inputFile.toPath())
                    .stream()
                    .map(TreePattern::fromString)
                    .collect(Collectors.toList());
    }
}
