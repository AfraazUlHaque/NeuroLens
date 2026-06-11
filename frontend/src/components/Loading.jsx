function Loading() {
    return (
        <div className="text-center mt-8">

            <div className="text-6xl animate-pulse">
                🧠
            </div>

            <h2 className="text-xl mt-4 text-cyan-300">
                AI is analyzing MRI...
            </h2>

            <p className="text-gray-400">
                Generating tumor segmentation
            </p>

        </div>
    );
}

export default Loading;