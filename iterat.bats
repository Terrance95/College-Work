#!/usr/bin/env bats

setup() {
    # Windows Process Safety: Kills any hung instances before recompiling
    taskkill //F //IM iterative_binarys.exe //T 2> /dev/null || true
    g++ -g iterative_binarys.cpp -o iterative_binarys.exe
}

teardown() {
    rm -f iterative_binarys.exe || true
}

@test "Worst Case 1: Target at the Start (Index 0)" {
    # 5 elements: 10 20 30 40 50 | Search for 10
    run bash -c "printf '5\n10 20 30 40 50\n10\n' | ./iterative_binarys.exe"
    
    [ "$status" -eq 0 ]
    [[ "$output" == *"element found at index 0"* ]]
}

@test "Worst Case 2: Target at the End (Index n-1)" {
    # 5 elements: 10 20 30 40 50 | Search for 50
    run bash -c "printf '5\n10 20 30 40 50\n50\n' | ./iterative_binarys.exe"
    
    [ "$status" -eq 0 ]
    [[ "$output" == *"element found at index 4"* ]]
}

@test "Worst Case 3: Element Not Found (Loop Exhaustion)" {
    # Searching for a missing high value
    run bash -c "printf '5\n10 20 30 40 50\n99\n' | ./iterative_binarys.exe"
    
    [ "$status" -eq 0 ]
    [[ "$output" == *"element not found"* ]]
}

@test "Boundary Case: Array of Size 1" {
    run bash -c "printf '1\n500\n500\n' | ./iterative_binarys.exe"
    
    [ "$status" -eq 0 ]
    [[ "$output" == *"element found at index 0"* ]]
}