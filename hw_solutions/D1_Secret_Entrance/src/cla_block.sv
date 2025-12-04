
module cla_block
(
    input logic [3:0] a, b,
    input logic carry_in,
    output logic [3:0] sum,
    output logic pg, gg
);
    logic [3:0] p, g, input_carry;
    assign input_carry[0] = carry_in;
    assign g =  a & b;
    assign p =  a | b;

    assign pg = &p;
    assign gg = g[3] | (g[2] & p[3]) | (g[1] & p[3] & p[2]) | (g[0] & p[3] & p[2] & p[1]);

    assign input_carry[1] = g[0] | (p[0] & input_carry[0]);
    assign input_carry[2] = g[1] | (p[1] & input_carry[1]);
    assign input_carry[3] = g[2] | (p[2] & input_carry[2]);

    generate
        for (genvar i = 0; i < 4; i++) begin
            full_adder FA (.a(a[i]), .b(b[i]), .cin(input_carry[i]), .sum(sum[i]));
        end
    endgenerate


endmodule