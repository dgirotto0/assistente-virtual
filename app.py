import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

def response(question):
    # Tokenizar a pergunta do usuário
    tokens = word_tokenize(question.lower())
    
    # Remover stop words
    stop_words = set(stopwords.words('portuguese'))
    tokens = [token for token in tokens if token not in stop_words]

    # Aplicar lematização para reduzir as palavras a suas formas base
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(token) for token in tokens]

    # Verificar mensagens de saudação
    greetings = ['bom', 'dia', 'tarde', 'noite', 'olá', 'ola', 'oi', 'tudo bem', 'olá!', 'ola!', 'ei', 'saudações', 'hello']
    if any(token in tokens for token in greetings):
        return "Olá! Em que posso ajudar?"

    # Respostas específicas
    services_keywords = ['serviço', 'serviços', 'troca', 'óleo', 'filtros', 'higienização', 'mecânica', 'manutenção', 'reparos', 'inspeção', 'motor', 'freios', 'suspensão', 'amortecedores', 'bateria']
    location_keywords = ['localização', 'local', 'endereço', 'onde', 'fica', 'situada', 'localiza']
    hours_keywords = ['horário', 'horários', 'funcionamento', 'abre', 'fecha', 'abertura', 'fechamento', 'horario', 'horarios', 'dias', 'horas']
    phone_keywords = ['telefone', 'contato', 'número', 'telefone', 'numero', 'whatsapp']
    payment_keywords = ['pagamento', 'formas', 'pix', 'cartão', 'dinheiro', 'parcela', 'cartao', 'crédito', 'débito', 'credit', 'debit', 'parcelamento']

    if any(token in tokens for token in services_keywords):
        return ("Os serviços da ItaOleo incluem troca de óleo, filtros, óleo de câmbio automático, "
                "higienização, manutenção geral, reparos de motor, freios, suspensão, amortecedores, "
                "e verificação de bateria. Atendemos também empresas com prazos diferenciados. Estamos prontos para atender suas necessidades.")
    elif any(token in tokens for token in location_keywords):
        return "A ItaOleo está localizada na Av. Vinte e Nove de Abril, 458 - Vila Santa Clara, Itatiba - SP. Venha nos visitar!"
    elif any(token in tokens for token in hours_keywords):
        return "O horário de funcionamento da ItaOleo é de segunda a sexta, das 8h às 17h, e aos sábados, das 8h às 12h. Esperamos por você!"
    elif any(token in tokens for token in phone_keywords):
        return "O telefone da ItaOleo é (11) 4534-1546. Fique à vontade para nos ligar e fazer um orçamento!"
    elif any(token in tokens for token in payment_keywords):
        return ("Aceitamos diversas formas de pagamento, incluindo Pix, cartões de crédito e débito, dinheiro, "
                "e também oferecemos parcelamento no cartão. Facilidades de pagamento para sua conveniência.")
    else:
        return ("Desculpe, não entendi sua pergunta. Você gostaria de saber sobre nossos serviços, localização, "
                "horário de funcionamento, formas de pagamento ou telefone de contato?")