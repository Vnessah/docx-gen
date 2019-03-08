from StringIO import StringIO
from docx.shared import Cm
from docxtpl import DocxTemplate, InlineImage

def get_context():
    """ You can generate your context separately since you may deal with a lot 
        of documents. You can carry out computations, etc in here and make the
        context look like the sample below.
    """
    return {
        'invoice_no': 12345,
        'date': '30 Mar',
        'due_date': '30 Apr',
        'name': 'Jane Doe',
        'address': '123 Quiet Lane',
        'subtotal': 335,
        'tax_amt': 10,
        'total': 345,
        'amt_paid': 100,
        'amt_due': 245,
        'row_contents': [
            {
                'description': 'Eggs',
                'quantity': 30,
                'rate': 5,
                'amount': 150
            }, {
                'description': 'All Purpose Flour',
                'quantity': 10,
                'rate': 15,
                'amount': 150
            }, {
                'description': 'Eggs',
                'quantity': 5,
                'rate': 7,
                'amount': 35
            }
        ]
    }


def from_template(template, signature):
    target_file = StringIO()

    template = DocxTemplate(template)
    context = get_context()  # gets the context used to render the document

    img_size = Cm(7)  # sets the size of the image
    sign = InlineImage(template, signature, img_size)
    context['signature'] = sign  # adds the InlineImage object to the context

    target_file = StringIO()
    template.render(context)
    template.save(target_file)

    return target_file
