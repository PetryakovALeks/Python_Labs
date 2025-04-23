using System;
using System.Data;
using System.Drawing;
using System.Windows.Forms;

namespace di5
{
    public partial class AdminMatchesForm : Form
    {
        public AdminMatchesForm()
        {
            InitializeComponent();
            SetupUI();
        }

        private void SetupUI()
        {
            this.Text = "Редактирование матчей";
            this.Size = new Size(800, 500);
            this.StartPosition = FormStartPosition.CenterScreen;

            // Пример DataGridView для редактирования матчей
            DataGridView dataGridView = new DataGridView
            {
                Dock = DockStyle.Top,
                Height = 150,
                AllowUserToAddRows = true,
                AllowUserToDeleteRows = true,
                DataSource = GetSampleData()
            };

            Button btnSave = new Button
            {
                Text = "Сохранить изменения",
                Dock = DockStyle.Bottom,
                Height = 40,
                BackColor = Color.Salmon,
                ForeColor = Color.White
            };

            btnSave.Click += (s, e) => SaveChanges(dataGridView);

            this.Controls.AddRange(new Control[] { dataGridView, btnSave });
        }

        private DataTable GetSampleData()
        {
            DataTable table = new DataTable();
            table.Columns.Add("Дата");
            table.Columns.Add("Матч");
            table.Columns.Add("Стадион");
            table.Columns.Add("Доступные билеты");

            table.Rows.Add("15.05.2023", "Барселона - Реал Мадрид", "Камп Ноу", "15000");
            table.Rows.Add("22.05.2023", "Барселона - Атлетико", "Камп Ноу", "12000");

            return table;
        }

        private void SaveChanges(DataGridView grid)
        {
            // Здесь должна быть логика сохранения в БД/файл
            MessageBox.Show("Изменения сохранены", "Успех", MessageBoxButtons.OK, MessageBoxIcon.Information);
            this.Close();
        }
    }
}