import {useState} from 'react';

function  CheckForm(){
    const [loading, setLoading] = useState(false);
    const [errorMessage, setErrorMessage] = useState('');
    const[formData,setFormData]=useState({
        name:'',
        tel:'',
        address:''
    });
    
    const [errors,setErrors]=useState({
        name:'',
        tel:'',
        address:''
    });
    const [isSuccess,setSucces]=useState(false)

    const handleChange=(e)=>{
            const {name,value}=e.target;
            setFormData({
                ...formData,
                [name]:value
        });
    }

    const Validate=()=>{
        const newErrors={};

        if (!formData.name){
            newErrors.name='Введите имя'
        }else if (formData.name.length<2){
            newErrors.name='Имя должно содержать больше 2-х смволов'
        }
        if (!formData.tel){
            newErrors.tel='Введите номер телефона'}
            else if (formData.tel.length < 11){
            newErrors.tel='Номер телефона неккоректен, минимум 11 символов'
        }
        if (!formData.address){
            newErrors.address='Введите адрес'
        } else if(formData.address.length<5){
            newErrors.address='Введите реальный адрес'
        }
        return newErrors;
    };
       

    const handleSubmit= async (e)=>{
        e.preventDefault();
        const newErrors=Validate();
        setErrors(newErrors)
        if (Object.keys(newErrors).length!=0){
            console.log('Форма не валидна', formData);
            return;
        }
        setLoading(true);
        try{
            const response=await fetch('http://localhost:8000/api/checkout',{
                 method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify(formData)
                });
            if(!response.ok){
                throw new Error('Что то пошло не так')
            }
            else {
                setSucces(true)
            }
            
        }
        catch(error){
            console.error('Ошибка сети',error);
            setErrorMessage('Сервер недоступен')
        }
        finally{
            setLoading(false)
        }}
   
    if (isSuccess) return <div>Заказ оформлен!</div>
    return(
    <form onSubmit={handleSubmit}>
            <fieldset>
                <legend>
                    Контактная информация
                </legend>
                <label htmlFor="name" className="label">Имя</label>
                <input 
                    name="name" 
                    value={formData.name}
                    onChange={handleChange}
                />
                {errors.name && <span className="errors">{errors.name}</span>}
                <label htmlFor="tel" className="label">Телефон</label>
                <input 
                    name="tel" 
                    value={formData.tel}
                    onChange={handleChange}
                />
                {errors.tel && <span className="errors">{errors.tel}</span>}
            </fieldset>

            <fieldset>
                <legend>Доставка</legend>
                <label htmlFor="address" className="label">Адрес</label>
                <input 
                    name="address" 
                    value={formData.address}
                    onChange={handleChange}
                />
            {errors.address && <span className="errors">{errors.address}</span>}
            </fieldset>
            {errorMessage && <p className="error">{errorMessage}</p>}
            <button type ="submit" disabled={loading}>{loading ? "Загрузка" : "Отправить"}</button>
        </form>
);
}
export default CheckForm;



    
