module full_adder
(
    input logic a,
    input logic b,
    input logic cin,
    output logic sum
);

    assign sum = a ^ b ^ cin;

endmodule