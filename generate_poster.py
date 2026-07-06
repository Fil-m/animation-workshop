import os
import requests

def generate_qr_codes():
    print("Generating QR codes for Animation Workshop...")
    urls = {
        "website": "https://fil-m.github.io/animation-workshop/",
        "organizer": "https://t.me/robosapiens8"
    }
    
    # Try using qrcode library if installed
    try:
        import qrcode
        print("Using local 'qrcode' library.")
        for name, url in urls.items():
            qr = qrcode.QRCode(version=1, box_size=10, border=1)
            qr.add_data(url)
            qr.make(fit=True)
            img = qr.make_image(fill_color="black", back_color="white")
            img.save(f"assets/qr_{name}.png")
            print(f"Generated assets/qr_{name}.png")
    except ImportError:
        print("Local 'qrcode' library not found. Fetching from QR Server API...")
        os.makedirs("assets", exist_ok=True)
        for name, url in urls.items():
            api_url = f"https://api.qrserver.com/v1/create-qr-code/?size=300x300&data={url}"
            try:
                response = requests.get(api_url, timeout=10)
                if response.status_code == 200:
                    with open(f"assets/qr_{name}.png", "wb") as f:
                        f.write(response.content)
                    print(f"Downloaded assets/qr_{name}.png")
                else:
                    print(f"Failed to fetch QR code for {name}: HTTP {response.status_code}")
            except Exception as e:
                print(f"Error fetching QR code for {name}: {e}")

def create_html_poster():
    print("Creating HTML poster...")
    html_content = """<!DOCTYPE html>
<html lang="uk">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Анімаційна майстерня — Афіша А4</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800;900&display=swap" rel="stylesheet">
    <style>
        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }
        body {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Arial, sans-serif;
            color: #000000;
            background: #ffffff;
            line-height: 1.4;
            padding: 0;
            -webkit-print-color-adjust: exact;
            print-color-adjust: exact;
        }
        
        @page {
            size: A4;
            margin: 12mm 15mm;
        }
        
        .poster-container {
            width: 100%;
            max-width: 210mm;
            min-height: 297mm;
            margin: 0 auto;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }

        /* Header styling */
        .header {
            text-align: center;
            border-bottom: 3px solid #000;
            padding-bottom: 8px;
            margin-bottom: 16px;
        }
        .header-badge {
            display: inline-block;
            border: 2px solid #000;
            padding: 4px 12px;
            font-weight: 700;
            font-size: 13px;
            text-transform: uppercase;
            letter-spacing: 1px;
            margin-bottom: 8px;
        }
        .header h1 {
            font-size: 36px;
            font-weight: 900;
            letter-spacing: -1px;
            text-transform: uppercase;
            line-height: 1.1;
            margin-bottom: 4px;
        }
        .header .tagline {
            font-size: 16px;
            font-weight: 600;
            margin-top: 4px;
        }

        /* Main content */
        .main-content {
            flex-grow: 1;
            display: flex;
            flex-direction: column;
            gap: 14px;
        }

        .section-box {
            border: 2px solid #000;
            padding: 12px 16px;
            background: #ffffff;
        }
        
        .section-title {
            font-size: 18px;
            font-weight: 800;
            text-transform: uppercase;
            border-bottom: 2px solid #000;
            padding-bottom: 2px;
            margin-bottom: 8px;
            display: inline-block;
        }

        /* Info items */
        .info-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 12px;
        }
        .info-item {
            text-align: center;
        }
        .info-item strong {
            display: block;
            font-size: 13px;
            font-weight: 700;
            text-transform: uppercase;
            margin-bottom: 2px;
        }
        .info-item p {
            font-size: 12.5px;
            line-height: 1.25;
        }

        /* Steps */
        .steps-grid {
            display: grid;
            grid-template-columns: repeat(5, 1fr);
            gap: 8px;
        }
        .step-item {
            text-align: center;
            border: 1px solid #ddd;
            padding: 8px;
            border-radius: 8px;
            background: #fafafa;
        }
        .step-num {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            width: 24px;
            height: 24px;
            border-radius: 50%;
            background: #000;
            color: #fff;
            font-weight: 800;
            font-size: 12px;
            margin-bottom: 4px;
        }
        .step-item h4 {
            font-size: 11.5px;
            font-weight: 700;
            margin-bottom: 2px;
        }
        .step-item p {
            font-size: 10px;
            color: #444;
            line-height: 1.2;
        }

        /* Details */
        .details-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 8px 16px;
        }
        .detail-item {
            font-size: 12.5px;
        }
        .detail-item strong {
            display: block;
            font-size: 13.5px;
            font-weight: 700;
        }

        /* Security Box */
        .security-box {
            border: 2px dashed #000;
            background: #fdfdfd;
            padding: 12px;
            display: flex;
            align-items: flex-start;
            gap: 10px;
        }
        .security-icon {
            font-size: 20px;
            line-height: 1;
        }
        .security-text h3 {
            font-size: 15px;
            font-weight: 800;
            text-transform: uppercase;
            margin-bottom: 2px;
        }
        .security-text p {
            font-size: 12.5px;
            font-weight: 600;
            line-height: 1.3;
        }

        /* QR section */
        .qr-section {
            border-top: 2px solid #000;
            padding-top: 12px;
            margin-top: 10px;
        }
        .qr-title {
            text-align: center;
            font-size: 14px;
            font-weight: 800;
            text-transform: uppercase;
            margin-bottom: 10px;
        }
        .qr-grid {
            display: flex;
            justify-content: center;
            gap: 60px;
        }
        .qr-card {
            text-align: center;
            max-width: 150px;
        }
        .qr-image-wrapper {
            border: 2px solid #000;
            padding: 4px;
            background: #fff;
            display: inline-block;
            margin-bottom: 4px;
        }
        .qr-card img {
            width: 100px;
            height: 100px;
            display: block;
        }
        .qr-card h4 {
            font-size: 13px;
            font-weight: 700;
            text-transform: uppercase;
            margin-bottom: 2px;
        }
        .qr-card p {
            font-size: 10.5px;
            color: #444;
            line-height: 1.2;
        }

        .footer-note {
            text-align: center;
            font-size: 11px;
            font-weight: 600;
            margin-top: 12px;
            border-top: 1px solid #ddd;
            padding-top: 6px;
        }
        .impressum {
            font-size: 9px;
            font-weight: normal;
            color: #666;
            display: block;
            margin-top: 4px;
        }

        /* Print controls banner */
        .no-print-banner {
            background: #f0f0f0;
            border: 1px solid #ccc;
            padding: 12px;
            margin-bottom: 20px;
            text-align: center;
            font-size: 14px;
        }
        .no-print-banner button {
            background: #000;
            color: #fff;
            border: none;
            padding: 8px 16px;
            font-weight: 700;
            cursor: pointer;
            margin-top: 8px;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }
        .no-print-banner button:hover {
            background: #333;
        }

        @media print {
            .no-print-banner {
                display: none !important;
            }
            body {
                padding: 0;
            }
            .poster-container {
                min-height: auto;
            }
        }
    </style>
</head>
<body>

    <div class="no-print-banner">
        <strong>Афіша Анімаційної майстерні підготовлена до друку на форматі A4 (чорно-біла).</strong><br>
        Відкрийте цю сторінку в браузері, натисніть кнопку нижче або комбінацію клавіш <strong>Ctrl + P</strong> і виберіть принтер або збереження в PDF.<br>
        <button onclick="window.print()">Друк / Зберегти як PDF</button>
    </div>

    <div class="poster-container">
        <div class="header">
            <div class="header-badge">📍 Karlsruhe · Безкоштовно · Для батьків та дітей</div>
            <h1>Анімаційна майстерня</h1>
            <p class="tagline">Батьки — найкращі вчителі. Анімація — інструмент.</p>
        </div>

        <div class="main-content">
            <div class="section-box">
                <div class="info-grid">
                    <div class="info-item">
                        <strong>📅 Розклад</strong>
                        <p>2 суботи на місяць<br>2 зустрічі по 2 години</p>
                    </div>
                    <div class="info-item">
                        <strong>📍 Локація</strong>
                        <p>Кав'ярня <i>Ja, genau!</i><br>Hirschstraße, 76133 KA</p>
                    </div>
                    <div class="info-item">
                        <strong>👶 Учасники</strong>
                        <p>Діти 6–12 років<br>у парі з батьками</p>
                    </div>
                </div>
            </div>

            <div class="section-box">
                <div class="section-title">Як усе проходить?</div>
                <div class="steps-grid">
                    <div class="step-item">
                        <div class="step-num">1</div>
                        <h4>Сценарій</h4>
                        <p>Вигадуємо сюжет та персонажів.</p>
                    </div>
                    <div class="step-item">
                        <div class="step-num">2</div>
                        <h4>Декорації</h4>
                        <p>Будуємо сцену з LEGO чи пластиліну.</p>
                    </div>
                    <div class="step-item">
                        <div class="step-num">3</div>
                        <h4>Зйомка</h4>
                        <p>Робимо покадрові знімки stop-motion.</p>
                    </div>
                    <div class="step-item">
                        <div class="step-num">4</div>
                        <h4>Монтаж</h4>
                        <p>Додаємо музику, звуки та титри.</p>
                    </div>
                    <div class="step-item">
                        <div class="step-num">5</div>
                        <h4>Показ</h4>
                        <p>Дивимося готовий мультик разом!</p>
                    </div>
                </div>
            </div>

            <div class="section-box">
                <div class="section-title">Чому це важливо та корисно?</div>
                <div class="details-grid">
                    <div class="detail-item">
                        <strong>🧠 Розвиток мислення та логіки</strong>
                        Створення анімації вчить планувати дії, бачити причинно-наслідкові зв'язки та логічно мислити.
                    </div>
                    <div class="detail-item">
                        <strong>🗣️ Мовлення та моторика</strong>
                        Придумування діалогів та озвучка розвивають мовлення. Мікрорухи фігурок тренують дрібну моторику.
                    </div>
                    <div class="detail-item">
                        <strong>📱 Спільний час без пасивного екрану</strong>
                        Вчимося перетворювати звичайний смартфон на корисний інструмент для сумісної родинної творчості.
                    </div>
                    <div class="detail-item">
                        <strong>🛠️ Що потрібно мати з собою?</strong>
                        Тільки телефон із додатком <i>Stop Motion Studio</i>. Усі матеріали для сцени ми надаємо на місці.
                    </div>
                </div>
            </div>

            <div class="security-box">
                <div class="security-icon">🔒</div>
                <div class="security-text">
                    <h3>Безпека неповнолітніх та Bildrechte (DSGVO)</h3>
                    <p>Зйомка дітей не проводиться без згоди батьків. Усі створені відеоролики та фотоматеріали залишаються виключною власністю родин і не публікуються в інтернеті без вашої письмової згоди.</p>
                </div>
            </div>
        </div>

        <div class="qr-section">
            <div class="qr-title">Усього 6–7 місць (за попередньою реєстрацією). Запишіться заздалегідь:</div>
            <div class="qr-grid">
                <div class="qr-card">
                    <div class="qr-image-wrapper">
                        <img src="assets/qr_website.png" alt="QR Website">
                    </div>
                    <h4>Сайт майстерні</h4>
                    <p>Приклади готових мультиків та розгорнуті деталі</p>
                </div>
                
                <div class="qr-card">
                    <div class="qr-image-wrapper">
                        <img src="assets/qr_organizer.png" alt="QR Contact">
                    </div>
                    <h4>Записатися</h4>
                    <p>Напишіть організатору в Telegram: @robosapiens8</p>
                </div>
            </div>
        </div>

        <div class="footer-note">
            Анімаційна майстерня для батьків та дітей · Karlsruhe · Приватна некомерційна ініціатива
            <span class="impressum">Impressum: Taras Moskalenko, Goethestraße 17, 76227 Karlsruhe | moskalenko.t.o@gmail.com</span>
        </div>
    </div>

</body>
</html>
"""
    with open("poster.html", "w", encoding="utf-8") as f:
        f.write(html_content)
    print("Created poster.html")

def create_pdf_poster():
    print("Creating PDF poster...")
    try:
        from reportlab.lib.pagesizes import A4
        from reportlab.lib.units import mm
        from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image
        from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
        from reportlab.lib import colors
        from reportlab.pdfbase import pdfmetrics
        from reportlab.pdfbase.ttfonts import TTFont
    except ImportError:
        print("Reportlab not available. Cannot generate PDF directly. Use HTML poster and print as PDF.")
        return

    # Check for Arial font on Windows
    arial_path = "C:\\Windows\\Fonts\\arial.ttf"
    arial_bold_path = "C:\\Windows\\Fonts\\arialbd.ttf"
    
    if os.path.exists(arial_path) and os.path.exists(arial_bold_path):
        pdfmetrics.registerFont(TTFont('Arial', arial_path))
        pdfmetrics.registerFont(TTFont('Arial-Bold', arial_bold_path))
        FONT_NORMAL = 'Arial'
        FONT_BOLD = 'Arial-Bold'
        print("Using system Arial font for Cyrillic support.")
    else:
        FONT_NORMAL = 'Helvetica'
        FONT_BOLD = 'Helvetica-Bold'
        print("Arial font not found. Falling back to Helvetica (Cyrillic characters might not render).")

    doc = SimpleDocTemplate(
        "animation_workshop_poster_a4.pdf",
        pagesize=A4,
        rightMargin=15*mm,
        leftMargin=15*mm,
        topMargin=12*mm,
        bottomMargin=12*mm
    )

    styles = getSampleStyleSheet()

    # Define custom styles
    title_style = ParagraphStyle('MainTitle', parent=styles['Normal'], fontName=FONT_BOLD, fontSize=28, leading=32, alignment=1)
    
    badge_style = ParagraphStyle('Badge', parent=styles['Normal'], fontName=FONT_BOLD, fontSize=9.5, leading=11.5, alignment=1)
    tagline_style = ParagraphStyle('Tagline', parent=styles['Normal'], fontName=FONT_BOLD, fontSize=12, leading=15, alignment=1)
    
    sec_title_style = ParagraphStyle('SecTitle', parent=styles['Normal'], fontName=FONT_BOLD, fontSize=11.5, leading=13.5, spaceAfter=3)
    body_style = ParagraphStyle('BodyTextCustom', parent=styles['Normal'], fontName=FONT_NORMAL, fontSize=8.5, leading=11)
    
    step_title_style = ParagraphStyle('StepTitle', parent=styles['Normal'], fontName=FONT_BOLD, fontSize=8.5, leading=10.5, alignment=1)
    step_body_style = ParagraphStyle('StepBody', parent=styles['Normal'], fontName=FONT_NORMAL, fontSize=7.5, leading=9.5, alignment=1)
    
    detail_bold_style = ParagraphStyle('DetailBold', parent=styles['Normal'], fontName=FONT_BOLD, fontSize=9.5, leading=12)
    detail_body_style = ParagraphStyle('DetailBody', parent=styles['Normal'], fontName=FONT_NORMAL, fontSize=8.5, leading=11.5)
    
    security_title_style = ParagraphStyle('SecurTitle', parent=styles['Normal'], fontName=FONT_BOLD, fontSize=10.5, leading=12.5, spaceAfter=1)
    security_body_style = ParagraphStyle('SecurBody', parent=styles['Normal'], fontName=FONT_BOLD, fontSize=9, leading=11.5)
    
    qr_title_style = ParagraphStyle('QRTitle', parent=styles['Normal'], fontName=FONT_BOLD, fontSize=10, leading=12, alignment=1)
    qr_label_style = ParagraphStyle('QRLabel', parent=styles['Normal'], fontName=FONT_BOLD, fontSize=9, leading=11, alignment=1)
    qr_desc_style = ParagraphStyle('QRDesc', parent=styles['Normal'], fontName=FONT_NORMAL, fontSize=8, leading=9.5, alignment=1)
    
    footer_style = ParagraphStyle('FooterStyle', parent=styles['Normal'], fontName=FONT_NORMAL, fontSize=7.5, leading=9, alignment=1, textColor=colors.HexColor('#555555'))

    story = []

    # 1. Header Badge
    badge_p = Paragraph("📍 KARLSRUHE · БЕЗКОШТОВНО · ДЛЯ БАТЬКІВ ТА ДІТЕЙ", badge_style)
    badge_table = Table([[badge_p]], colWidths=[100*mm])
    badge_table.setStyle(TableStyle([
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('BOX', (0,0), (-1,-1), 1.5, colors.black),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
    ]))
    badge_table.hAlign = 'CENTER'
    story.append(badge_table)
    story.append(Spacer(1, 3*mm))

    # 2. Main Title: АНІМАЦІЙНА МАЙСТЕРНЯ
    story.append(Paragraph("АНІМАЦІЙНА МАЙСТЕРНЯ", title_style))
    story.append(Spacer(1, 2.5*mm))

    # Tagline
    story.append(Paragraph("Батьки — найкращі вчителі. Анімація — інструмент.", tagline_style))
    story.append(Spacer(1, 2.5*mm))

    # Thin line under header
    line_table = Table([[""]], colWidths=[176*mm], rowHeights=[2])
    line_table.setStyle(TableStyle([
        ('LINEBELOW', (0,0), (-1,-1), 2, colors.black),
        ('BOTTOMPADDING', (0,0), (-1,-1), 0),
        ('TOPPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(line_table)
    story.append(Spacer(1, 4*mm))

    # 3. Section 1: Info grid (3 columns)
    info_th1 = Paragraph("<b>📅 РОЗКЛАД</b>", step_title_style)
    info_tb1 = Paragraph("2 суботи на місяць<br/>2 зустрічі по 2 години", step_body_style)
    
    info_th2 = Paragraph("<b>📍 ЛОКАЦІЯ</b>", step_title_style)
    info_tb2 = Paragraph("Кав'ярня <i>Ja, genau!</i><br/>Hirschstraße, 76133 KA", step_body_style)
    
    info_th3 = Paragraph("<b>👶 УЧАСНИКИ</b>", step_title_style)
    info_tb3 = Paragraph("Діти 6–12 років<br/>у парі з батьками", step_body_style)

    sec1_content = [
        [info_th1, info_th2, info_th3],
        [info_tb1, info_tb2, info_tb3]
    ]
    sec1_table = Table(sec1_content, colWidths=[58*mm, 58*mm, 58*mm])
    sec1_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('BOX', (0,0), (-1,-1), 1.5, colors.black),
        ('TOPPADDING', (0,0), (-1,0), 6),
        ('BOTTOMPADDING', (0,0), (-1,0), 2),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,1), (-1,-1), 6),
        ('TOPPADDING', (0,1), (-1,-1), 2),
    ]))
    sec1_table.hAlign = 'CENTER'
    story.append(sec1_table)
    story.append(Spacer(1, 4*mm))

    # 4. Section 2: How it works (5 columns)
    step1 = [
        Paragraph("<font size=10><b>1</b></font>", step_title_style),
        Paragraph("<b>Сценарій</b>", step_title_style),
        Paragraph("Вигадуємо сюжет та персонажів.", step_body_style)
    ]
    step2 = [
        Paragraph("<font size=10><b>2</b></font>", step_title_style),
        Paragraph("<b>Декорації</b>", step_title_style),
        Paragraph("Будуємо сцену з LEGO чи пластиліну.", step_body_style)
    ]
    step3 = [
        Paragraph("<font size=10><b>3</b></font>", step_title_style),
        Paragraph("<b>Зйомка</b>", step_title_style),
        Paragraph("Робимо покадрові знімки stop-motion.", step_body_style)
    ]
    step4 = [
        Paragraph("<font size=10><b>4</b></font>", step_title_style),
        Paragraph("<b>Монтаж</b>", step_title_style),
        Paragraph("Додаємо музику, звуки та титри.", step_body_style)
    ]
    step5 = [
        Paragraph("<font size=10><b>5</b></font>", step_title_style),
        Paragraph("<b>Показ</b>", step_title_style),
        Paragraph("Дивимося готовий мультик разом!", step_body_style)
    ]

    sec2_content = [
        [Paragraph("ЯК УСЕ ПРОХОДИТЬ?", sec_title_style), "", "", "", ""],
        [step1, step2, step3, step4, step5]
    ]
    sec2_table = Table(sec2_content, colWidths=[35*mm, 35*mm, 35*mm, 35*mm, 35*mm])
    sec2_table.setStyle(TableStyle([
        ('SPAN', (0,0), (4,0)),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('BOX', (0,0), (-1,-1), 1.5, colors.black),
        ('TOPPADDING', (0,0), (-1,0), 6),
        ('BOTTOMPADDING', (0,0), (-1,0), 2),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,1), (-1,-1), 8),
        ('TOPPADDING', (0,1), (-1,-1), 4),
    ]))
    sec2_table.hAlign = 'CENTER'
    story.append(sec2_table)
    story.append(Spacer(1, 4*mm))

    # 5. Section 3: Why it is important
    sec3_content = [
        [Paragraph("ЧОМУ ЦЕ ВАЖЛИВО ТА КОРИСНО?", sec_title_style), ""],
        [
            Paragraph("<b>🧠 Розвиток мислення та логіки</b><br/>Створення анімації вчить планувати дії, бачити причинно-наслідкові зв'язки та логічно мислити.", body_style),
            Paragraph("<b>🗣️ Мовлення та моторика</b><br/>Придумування діалогів та озвучка розвивають мовлення. Мікрорухи фігурок тренують дрібну моторику.", body_style)
        ],
        [
            Paragraph("<b>📱 Спільний час без пасивного екрану</b><br/>Вчимося перетворювати звичайний смартфон на корисний інструмент для сумісної родинної творчості.", body_style),
            Paragraph("<b>🛠️ Що потрібно мати з собою?</b><br/>Тільки телефон із додатком <i>Stop Motion Studio</i>. Усі матеріали для сцени ми надаємо на місці.", body_style)
        ]
    ]
    sec3_table = Table(sec3_content, colWidths=[88*mm, 88*mm])
    sec3_table.setStyle(TableStyle([
        ('SPAN', (0,0), (1,0)),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('BOX', (0,0), (-1,-1), 1.5, colors.black),
        ('TOPPADDING', (0,0), (-1,0), 6),
        ('BOTTOMPADDING', (0,0), (-1,0), 2),
        ('LEFTPADDING', (0,0), (-1,-1), 10),
        ('RIGHTPADDING', (0,0), (-1,-1), 10),
        ('BOTTOMPADDING', (0,-1), (-1,-1), 8),
        ('TOPPADDING', (0,1), (-1,-1), 4),
        ('BOTTOMPADDING', (0,1), (-1,-2), 4),
    ]))
    sec3_table.hAlign = 'CENTER'
    story.append(sec3_table)
    story.append(Spacer(1, 4*mm))

    # 6. Security box (GDPR)
    security_p1 = Paragraph("Безпека неповнолітніх та Bildrechte (DSGVO)", security_title_style)
    security_p2 = Paragraph("Зйомка дітей не проводиться без згоди батьків. Усі створені відеоролики та фотоматеріали залишаються виключною власністю родин і не публікуються в інтернеті без вашої письмової згоди.", security_body_style)
    
    security_table = Table([[security_p1], [security_p2]], colWidths=[176*mm])
    security_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('BOX', (0,0), (-1,-1), 1.5, colors.black),
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#f9f9f9')),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('LEFTPADDING', (0,0), (-1,-1), 10),
        ('RIGHTPADDING', (0,0), (-1,-1), 10),
    ]))
    security_table.hAlign = 'CENTER'
    story.append(security_table)
    story.append(Spacer(1, 4*mm))

    # Helper function to frame images tightly
    def make_boxed_image(path):
        img = Image(path, width=22*mm, height=22*mm)
        t = Table([[img]], colWidths=[24*mm], rowHeights=[24*mm])
        t.setStyle(TableStyle([
            ('ALIGN', (0,0), (-1,-1), 'CENTER'),
            ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
            ('BOX', (0,0), (-1,-1), 1, colors.black),
            ('LEFTPADDING', (0,0), (-1,-1), 0),
            ('RIGHTPADDING', (0,0), (-1,-1), 0),
            ('TOPPADDING', (0,0), (-1,-1), 0),
            ('BOTTOMPADDING', (0,0), (-1,-1), 0),
        ]))
        return t

    # 7. QR Section
    story.append(Paragraph("Усього 6–7 місць (за попередньою реєстрацією). Запишіться заздалегідь:", qr_title_style))
    story.append(Spacer(1, 3*mm))

    qr1 = make_boxed_image("assets/qr_website.png")
    qr2 = make_boxed_image("assets/qr_organizer.png")

    qr_table_data = [
        [qr1, qr2],
        [
            Paragraph("САЙТ МАЙСТЕРНІ", qr_label_style),
            Paragraph("ЗАПИСАТИСЯ", qr_label_style)
        ],
        [
            Paragraph("Приклади готових мультиків та розгорнуті деталі", qr_desc_style),
            Paragraph("Напишіть організатору в Telegram: @robosapiens8", qr_desc_style)
        ]
    ]
    qr_table = Table(qr_table_data, colWidths=[88*mm, 88*mm])
    qr_table.setStyle(TableStyle([
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('BOTTOMPADDING', (0,0), (-1,0), 3),
        ('BOTTOMPADDING', (0,1), (-1,1), 1),
        ('TOPPADDING', (0,1), (-1,-1), 3),
    ]))
    qr_table.hAlign = 'CENTER'
    story.append(qr_table)
    story.append(Spacer(1, 4*mm))

    # Separator line
    sep_table = Table([[""]], colWidths=[176*mm], rowHeights=[1])
    sep_table.setStyle(TableStyle([
        ('LINEBELOW', (0,0), (-1,-1), 1, colors.HexColor('#dddddd')),
        ('BOTTOMPADDING', (0,0), (-1,-1), 0),
        ('TOPPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(sep_table)
    story.append(Spacer(1, 3*mm))

    # 8. Footer
    footer_p = Paragraph("Анімаційна майстерня для батьків та дітей · Karlsruhe · Приватна некомерційна ініціатива<br/><font size=6.5 color='#666666'>Impressum: Taras Moskalenko, Goethestraße 17, 76227 Karlsruhe | moskalenko.t.o@gmail.com</font>", footer_style)
    story.append(footer_p)

    doc.build(story)
    print("Created animation_workshop_poster_a4.pdf")

if __name__ == "__main__":
    os.makedirs("assets", exist_ok=True)
    generate_qr_codes()
    create_html_poster()
    create_pdf_poster()
