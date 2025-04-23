using System;
using System.Drawing;
using System.Windows.Forms;

namespace di5
{
    public partial class AdminPanelForm : Form
    {
        public AdminPanelForm()
        {
            InitializeComponent();
            SetupUI();
        }

        private void SetupUI()
        {
            this.Text = "Панель администратора";
            this.Size = new Size(600, 400);
            this.StartPosition = FormStartPosition.CenterScreen;


            Button btnEditMatches = new Button
            {
                Text = "Редактировать матчи",
                Location = new Point(50, 50),
                Size = new Size(200, 50),
                BackColor = Color.FromArgb(128, 128, 255),
                ForeColor = Color.White,
                Font = new Font("Arial", 10, FontStyle.Bold)
            };

            Button btnEditTickets = new Button
            {
                Text = "Управление билетами",
                Location = new Point(50, 120),
                Size = new Size(200, 50),
                BackColor = Color.FromArgb(128, 128, 255),
                ForeColor = Color.White,
                Font = new Font("Arial", 10, FontStyle.Bold)
            };

            Button btnLogout = new Button
            {
                Text = "Выйти",
                Location = new Point(50, 300),
                Size = new Size(100, 30),
                BackColor = Color.Salmon,
                ForeColor = Color.White
            };

            btnEditMatches.Click += (s, e) =>
            {
                AdminMatchesForm matchesForm = new AdminMatchesForm();
                matchesForm.ShowDialog();
            };

           

            btnLogout.Click += (s, e) => this.Close();

            this.Controls.AddRange(new Control[] { btnEditMatches, btnEditTickets, btnLogout });
        }
    }
}