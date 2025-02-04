import gradio as gr

def calculate_tax(income, marital_status, assets):
    if income <= 250000:
        tax = 0
    elif income <= 500000:
        tax = (income - 250000) * 0.05
    elif income <= 1000000:
        tax = (income - 500000) * 0.2 + 12500
    else:
        tax = (income - 1000000) * 0.3 + 112500
    
    if marital_status == "Married":
        tax *= 0.95
    
    total_asset_cost = 0
    for asset in assets:
        try:
            total_asset_cost += float(asset[1])
        except ValueError:
            continue
    
    tax -= total_asset_cost * 0.1
    
    return f"Your calculated tax is: ₹{tax:.2f}"

iface = gr.Interface(
    fn=calculate_tax,
    inputs=[
        gr.Number(label="Enter your annual income in INR"),
        gr.Radio(choices=["Single", "Married"], label="Marital Status"),
        gr.Dataframe(
            headers=["Item", "Cost"],
            datatype=["str", "number"],
            label="Assets Purchased this Year"
        )
    ],
    outputs=gr.Textbox(),
    title="Indian Tax Calculator",
    description="Calculate your income tax based on Indian tax rates."
)

iface.launch()
