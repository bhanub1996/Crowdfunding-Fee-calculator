from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate_fee():
    # Get form inputs
    transaction_fee = 2
    platform_fee = 5
    promotional_fee = int(request.form['promotional_fee'])
    curation_support = int(request.form['curation_support'])

    population_score = int(request.form['population_score'])
    service_score = int(request.form['service_score'])
    campaign_value_score = int(request.form['campaign_value_score'])
    check_items = request.form.getlist('checkbox')
    print(check_items)
    authenticity_score = sum(int(i) for i in check_items)
    
    print(authenticity_score)
    discount_score = authenticity_score + population_score + service_score + campaign_value_score
    print(discount_score)


    # Calculate total fee
    total_fee = transaction_fee + promotional_fee + (1-discount_score/100) * (platform_fee + curation_support)
    
    return render_template('result.html', total_fee=total_fee)

if __name__ == '__main__':
    app.run(debug=True)