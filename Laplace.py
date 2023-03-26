import sympy as sp

def laplace_transform_step_by_step(equation):
    t, s = sp.symbols('t s')
    F = sp.laplace_transform(equation, t, s, noconds=True)
    display_transform_steps(equation, F, "Laplace Transform")
    return F

def inverse_laplace_transform_step_by_step(equation):
    t, s = sp.symbols('t s')
    f = sp.inverse_laplace_transform(equation, s, t, noconds=True)
    display_transform_steps(equation, f, "Inverse Laplace Transform")
    return f

def display_transform_steps(input_equation, output_equation, transform_name):
    print(f"\n{transform_name} Steps:")
    print(f"Input: {input_equation}")
    print(f"Output: {output_equation}\n")

if __name__ == "__main__":
    t = sp.symbols('t')
    input_equation = sp.exp(-2 * t)
    
    # Calculate and display the Laplace Transform step by step
    F = laplace_transform_step_by_step(input_equation)

    # Calculate and display the Inverse Laplace Transform step by step
    f = inverse_laplace_transform_step_by_step(F)
