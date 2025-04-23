using System;
using System.Collections.Generic;
using System.Windows.Forms;
using static System.Windows.Forms.VisualStyles.VisualStyleElement;

namespace di5
{
    public partial class HelpForm : Form
    {
        private List<HelpTopic> topics;

        public HelpForm()
        {
            InitializeComponent();

            topics = new List<HelpTopic>
            {
                new HelpTopic
                {
                    Title = "История",
                    Content = "Раздел 'История' содержит информацию об основании команды, её развитии и успехах."
                },
                new HelpTopic
                {
                    Title = "Состав",
                    Content = "Раздел 'Состав' показывает текущих игроков, их номера, позиции и краткие биографии."
                },
                new HelpTopic
                {
                    Title = "Расписание матчей",
                    Content = "Здесь отображается календарь матчей: дата, время и место проведения игр."
                },
                new HelpTopic
                {
                    Title = "Мои билеты",
                    Content = "Раздел для управления вашими билетами: покупка, просмотр, сохранение в PDF."
                }
            };
        }

        private void HelpForm_Load(object sender, EventArgs e)
        {
            lstTopics.Items.Clear();
            lstTopics.Items.AddRange(topics.ToArray());
        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {
            lstTopics.Items.Clear();
            foreach (var topic in topics)
            {
                if (topic.Title.ToLower().Contains(txtSearch.Text.ToLower()) ||
                    topic.Content.ToLower().Contains(txtSearch.Text.ToLower()))
                {
                    lstTopics.Items.Add(topic);
                }
            }
        }

        private void lstTopics_SelectedIndexChanged(object sender, EventArgs e)
        {
            if (lstTopics.SelectedItem is HelpTopic selectedTopic)
            {
                rtbHelpText.Text = selectedTopic.Content;
            }
        }

        private void rtbHelpText_TextChanged(object sender, EventArgs e)
        {
            // Необязательно, можно оставить пустым
        }

        private void button1_Click(object sender, EventArgs e)
        {
            this.Close();

            // Создаем и показываем главную форму (например, MainForm)
            MainForm mainForm = new MainForm();
            mainForm.Show();
        }
    }

    public class HelpTopic
    {
        public string Title { get; set; }
        public string Content { get; set; }

        public override string ToString()
        {
            return Title;
        }
    }
}
