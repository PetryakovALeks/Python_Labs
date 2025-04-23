using System;
using System.Drawing;
using System.Linq;
using System.Windows.Forms;

namespace di5
{
    public partial class RaspForm : Form
    {
        public RaspForm()
        {
            InitializeComponent();
            SetupUI();
        }

        private void SetupUI()
        {
            this.Text = "Расписание матчей";
            this.Size = new Size(1500, 800);
            this.StartPosition = FormStartPosition.CenterScreen;
            this.BackColor = Color.WhiteSmoke;
        }

        // Кнопка "Назад" - возврат на главную форму
        private void back_but1_Click(object sender, EventArgs e)
        {
            this.Close();
            MainForm mainForm = Application.OpenForms.OfType<MainForm>().FirstOrDefault();
            mainForm?.Show();
        }

        // Кнопка "Домашние матчи"
        private void home_but_Click(object sender, EventArgs e)
        {
            home_but.BackColor = Color.Salmon;
            home_but.ForeColor = Color.White;
            home_but.FlatStyle = FlatStyle.Flat;
            home_but.FlatAppearance.BorderSize = 0;
            home_but.Font = new Font("Arial", 10, FontStyle.Bold);

            ShowMatches("Домашние");
        }

        // Кнопка "Гостевые матчи"
        private void away_but_Click(object sender, EventArgs e)
        {
            away_but.BackColor = Color.FromArgb(128, 128, 255);
            away_but.ForeColor = Color.White;
            away_but.FlatStyle = FlatStyle.Flat;
            away_but.FlatAppearance.BorderSize = 0;
            away_but.Font = new Font("Arial", 10, FontStyle.Bold);

            ShowMatches("Гостевые");
        }

        private void ShowMatches(string matchType)
        {
            this.Controls.Clear();

            // Заголовок
            Label titleLabel = new Label
            {
                Text = $"{matchType} матчи:",
                Font = new Font("Arial", 14, FontStyle.Bold),
                Location = new Point(1038, 545),
                AutoSize = true,
                BackColor = matchType == "Домашние" ? Color.Salmon : Color.FromArgb(128, 128, 255),
                ForeColor = Color.White,
                Padding = new Padding(5)
            };
            this.Controls.Add(titleLabel);

            string[] matches = matchType == "Домашние"
                ? new[] { "Барселона - Реал Мадрид", "Барселона - Атлетико", "Барселона - Валенсия" }
                : new[] { "Реал Мадрид - Барселона", "Атлетико - Барселона", "Севилья - Барселона" };

            for (int i = 0; i < matches.Length; i++)
            {
                Button matchButton = new Button
                {
                    Text = matches[i],
                    Location = new Point(50, 70 + i * 60),
                    Size = new Size(300, 50),
                    Tag = matches[i],
                    BackColor = i % 2 == 0 ? Color.Salmon : Color.FromArgb(128, 128, 255),
                    ForeColor = Color.White,
                    FlatStyle = FlatStyle.Flat,
                    Font = new Font("Arial", 10, FontStyle.Bold)
                };
                matchButton.FlatAppearance.BorderSize = 0;

                matchButton.Click += (s, e) =>
                {
                    ButTicketForm buyTicketForm = new ButTicketForm(matchButton.Text);
                    buyTicketForm.Show();
                    this.Hide();
                };

                this.Controls.Add(matchButton);
            }

            // Кнопка "Назад"
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
                this.Controls.Clear();
                InitializeComponent();
                SetupUI();
            };
            this.Controls.Add(backButton);
        }
    }
}