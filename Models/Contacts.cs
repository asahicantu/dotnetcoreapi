using System.ComponentModel.DataAnnotations;
namespace SQL.Models
{
    public class Contacts
    {
        [Key]
        public int Id { get; set; }       
        public string Name { get; set; }

        public string Mail { get; set; }

        public string Phone { get; set; }
    }
}