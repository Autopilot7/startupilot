export const Card: React.FC = () => {
    return (
        <div className="w-[70rem] bg-white rounded-2xl p-10 flex gap-x-8"> 
        <img src="https://static.ybox.vn/2023/5/3/1683723223801-336640751_761918645261000_7516888285445287067_n.jpg" 
        className="w-[10rem] rounded-full left-1"
        alt=""/>
        <div className="space-y-4">

            <div className="gap-x-4 flex items-end align-bottom">
            <h1 className="text-5xl font-bold"> Finful</h1>
            <div style={{width: '2px', height: '3rem', backgroundColor: '#DBDBDB'}}></div>
            <h2 className="text-2xl"> Finance</h2>
            </div>

            <p className="text-xl font-semibold"> a gamified app that teaches personal finance and investing through interactive lessons and quizzes,
                 making financial literacy fun, engaging, and easy to learn.
            </p>
        {/* Category Tag */}
        <div className="flex items-center">
                <span className="bg-orange-500 text-white text-sm mr-2 px-2.5 py-0.5 rounded">Incubator</span>
                <span className="bg-yellow-500 text-white text-sm mr-2 px-2.5 py-0.5 rounded">AY 2022-2023</span>
                <span className="bg-red-600 text-white text-sm mr-2 px-2.5 py-0.5 rounded">P1</span>
                <span className="bg-green-500 text-white text-sm mr-2 px-2.5 py-0.5 rounded">Active</span>
        </div>
        </div>
        
        </div>
    );
    }