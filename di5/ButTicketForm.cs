using System;
using System.Drawing;
using System.Linq;
using System.Windows.Forms;

namespace di5
{
    public partial class ButTicketForm : Form
    {
        public ButTicketForm()
        {
            InitializeComponent();
        }
        private string _matchName;

        public ButTicketForm(string matchName)
        {
            InitializeComponent();
            _matchName = matchName;
            SetupUI();
        }

        private void SetupUI()
        {
            this.Text = "Покупка билетов";
            this.Size = new Size(1200, 600);


            // Лейбл матча (Salmon)
            Label matchLabel = new Label
            {
                Text = $"Матч: {_matchName}",
                Font = new Font("Arial", 12, FontStyle.Bold),
                Location = new Point(20, 20),
                AutoSize = true,
                BackColor = Color.Salmon,
                ForeColor = Color.White,
                Padding = new Padding(5)
            };
            this.Controls.Add(matchLabel);

           

            // Кнопка Назад (128,128,255)
            Button backButton = new Button
            {
                Text = "Назад",
                Location = new Point(50, 500),
                Size = new Size(200, 50),
                BackColor = Color.FromArgb(128, 128, 255),
                ForeColor = Color.White,
                FlatStyle = FlatStyle.Flat,
                Font = new Font("Arial", 10, FontStyle.Bold)
            };
            backButton.FlatAppearance.BorderSize = 0;
            backButton.Click += (s, e) =>
            {
                this.Close();
                RaspForm raspForm = Application.OpenForms.OfType<RaspForm>().FirstOrDefault();
                raspForm?.Show();
            };
            this.Controls.Add(backButton);
        }

        // Ваши оригинальные методы без изменений
        private void Vip_But_Click(object sender, EventArgs e)
        {
            MyForm myForm = new MyForm();
            myForm.Show();
            this.Hide();
        }

        private void first_but_Click(object sender, EventArgs e)
        {
            MyForm myForm = new MyForm();
            myForm.Show();
            this.Hide();
        }

        private void sec_but_Click(object sender, EventArgs e)
        {
            MyForm myForm = new MyForm();
            myForm.Show();
            this.Hide();
        }

        private void third_but_Click(object sender, EventArgs e)
        {
            MyForm myForm = new MyForm();
            myForm.Show();
            this.Hide();
        }
    }
}