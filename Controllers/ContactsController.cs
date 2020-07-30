using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using SQL.Models;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Logging;

namespace SQL.Controllers
{
    [ApiController]
    [Route("[controller]")]

    public class ContactsController : Controller
    {
        private ContactsContext _context;

        public ContactsController(ContactsContext context)
        {
            _context = context;
        }

        [HttpGet]
        public ActionResult<IEnumerable<Contacts>> Get()
        {
            return _context.ContactSet.ToList();
        }


        [HttpGet("{id}")]
        public ActionResult<Contacts> Get(int id)
        {
            var selectedContact = (from c in _context.ContactSet where c.Id == id select c).FirstOrDefault();
            return selectedContact;
        }

        [HttpPost]
        public IActionResult Post([FromBody] Contacts value)
        {
            Contacts contact = value;
            _context.ContactSet.Add(contact);
            _context.SaveChanges();
            return Ok($"Contact has been added with value {contact.Id}");
        }

        [HttpPut]
        public IActionResult Put([FromBody] Contacts value)
        {
            var selectedContact = (from c in _context.ContactSet where c.Id == value.Id select c).FirstOrDefault();
            if (selectedContact != null)
            {
                selectedContact.Name = value.Name;
                selectedContact.Phone = value.Phone;
                selectedContact.Mail = value.Mail;
                _context.SaveChanges();
                return Ok($"Contact {value.Id} has been updated");
            }
            Response.StatusCode = 400;
            return Json(new { Success = false, Message = $"Contact with Id: {value.Id} not found" });
        }

        [HttpDelete("{id}")]
        public IActionResult Delete(int id)
        {
            var selectedElement = _context.ContactSet.Find(id);
            if (selectedElement != null)
            {
                _context.ContactSet.Remove(selectedElement);
                _context.SaveChanges();
                return Ok($"Contact {id} was successfully deleted");
            }
            Response.StatusCode = 400;
            return Json(new { Success = false, Message = $"Contact with Id: {id} not found" });
        }


        ~ContactsController()
        {
            _context.Dispose();
        }

    }
}